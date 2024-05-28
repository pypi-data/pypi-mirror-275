
# Import necessary modules and classes
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post, UserAddress, Progress
from django.shortcuts import render
import io, csv, os
import googlemaps
from geopy.geocoders import Nominatim
from django.shortcuts import render
from .forms import UserAddressForm

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


# View for the 'Our Team' page
def OurTeam(request):
    # Retrieve posts and users data and pass it to the template
    context = {
        'posts': Post.objects.all(),
        'users': User.objects.all()
    }
    return render(request, 'django_blog/our_team.html', context)


# List view for displaying posts on the home page
class PostListView(ListView):
    # Define the model and template name
    model = Post
    template_name = 'django_blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


# List view for displaying a user's posts
class UserPostListView(ListView):
    model = Post
    template_name = 'django_blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):  # Retrieve the user's posts based on the username
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# Detail view for displaying a single post
class PostDetailView(DetailView):
    model = Post


# Create view for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update view for updating a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check if the user is the author of the post
    def test_func(self):
    	post = self.get_object()
    	if self.request.user == post.author:
    		return True 
    	return False 


# Delete view for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):  # Check if the user is the author of the post
    	post = self.get_object()
    	if self.request.user == post.author:
    		return True 
    	return False 

# View for the home page
def home(request):
    return render(request, 'django_blog/home.html', {'title': 'home'})

# View for the 'proj-synopsis' page
def synopsis(request):
    return render(request, 'django_blog/proj_synopsis.html', {'title': 'proj-synopsis'})

# View for the 'proj-progress' page
def project_progress(request):
    return render(request, 'django_blog/proj_progress.html', {'title': 'proj-progress'})


# view for 'epidemiological data' page 
def epidemiological_data(request):

     # Fetch data from the Progress model
    progress_data = Progress.objects.all()

    # # Feltching all objects of Progress table to show graphs
    # progress_data = Progress.objects.all()

    # # Prepare data for the template
    # labels = [progress.name for progress in progress_data]
    # data = [progress.PercentageDownload for progress in progress_data]

    # # Print the contents of labels and data arrays for inspection
    # print("Labels:", labels)
    # print("Data:", data)
    
    context = {
        # 'labels': labels,
        # 'data': data,
        'title': 'epidem-data',
        'progress_data': progress_data
    }
    return render(request, 'django_blog/epidemiological_data.html', context)


# View for the 'data_repository' page
def data_repository(request):
    return render(request, 'django_blog/data_repository.html', {'title': 'data_repository'})


# Function to geocode addresses using Google Maps or Nominatim (geopy)
def get_coordinates(address):
    # Use googlemaps or Nominatim geocoder (geopy) to get latitude and longitude
    gmaps = googlemaps.Client(key='AIzaSyBDQUV4GhPxyJivBtOTiyn1fJyGjP8dhbA')  ### Replace with your API key ###
    geolocator = Nominatim(user_agent='django_blog')
    try:
        location = geolocator.geocode(address, timeout=1)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except geopy.exc.GeocoderTimedOut:
        print(f"Geocoding for address {address} timed out.")
        return None, None
    except Exception as e:
        print(f"Error geocoding address {address}: {str(e)}")
        return None, None


# view for geocoding when user add an address manually
def user_address_view(request):
    if request.method == 'POST':
        form = UserAddressForm(request.POST)
        if form.is_valid():
            address = f"{form.cleaned_data['house_number']} {form.cleaned_data['street']}, {form.cleaned_data['city']}, {form.cleaned_data['country']}"
            latitude, longitude = get_coordinates(address)
            form.instance.latitude = latitude
            form.instance.longitude = longitude
            form.save()
    else:
        form = UserAddressForm()
    return render(request, 'django_blog/user_address.html', {'form': form})


# View for CSV file upload and address geocoding
class CSVUploadView(View):
    def get(self, request):
        template_name = 'django_blog/importCSV.html'
        return render(request, template_name)

    def post(self, request):
        try:
            # Check if a file was provided
            if 'sent_file' not in request.FILES:
                error_message = "No file was uploaded."
                return render(request, 'django_blog/importCSV.html', {'error_message': error_message})

            uploaded_file = request.FILES['sent_file']
            
            # Check the file extension
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            if file_extension != '.csv':
                error_message = "Invalid file type. Please upload a CSV file."
                return render(request, 'django_blog/importCSV.html', {'error_message': error_message})

            paramFile = io.TextIOWrapper(uploaded_file.file)
            csv_reader = csv.DictReader(paramFile)

            list_of_dict = list(csv_reader)

            for row in list_of_dict:
                house_number = row['house_number']
                street = row['street']
                city = row['city']
                zipcode = row['zipcode']
                country = row['country']

                address = f"{house_number} {street}, {city}, {zipcode}, {country}"  # Corrected the address format
                print(f"Geocoding address: {address}")

                latitude, longitude = get_coordinates(address)
                print(f"Lat, long: {latitude}, {longitude}")

                UserAddress.objects.create(
                    house_number=house_number,
                    street=street,
                    city=city,
                    zipcode=zipcode,
                    country=country,
                    latitude=latitude,
                    longitude=longitude
                )

            success_message = "Addresses geocoded successfully."
            return render(request, 'django_blog/importCSV.html', {'success_message': success_message})

        except Exception as e:
            error_message = f"Error geocoding addresses: {str(e)}"
            return render(request, 'django_blog/importCSV.html', {'error_message': error_message})


