from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    user_address_view,
    data_repository,
    CSVUploadView, 
    epidemiological_data
)
from django_blog import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('team/', views.OurTeam, name='team-members'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('home/', views.home, name='blog-home'),
    path('synopsis/', views.synopsis, name='proj-synopsis'),
    path('progress/', views.project_progress, name='proj-progress'),
    path('epidemiological-data/', views.epidemiological_data, name='epidem-data'),
    path('user_address/', user_address_view, name='user_address'),
    path('data_repository/', views.data_repository, name='data_repository'),
    path('importCSV/', CSVUploadView.as_view(), name='importCSV')
    ]



