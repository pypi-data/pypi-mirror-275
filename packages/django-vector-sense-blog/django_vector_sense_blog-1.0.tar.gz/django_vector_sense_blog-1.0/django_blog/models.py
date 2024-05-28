from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

# Model for representing a blog post
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str_(self):
		return self.title


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

# Model for representing user addresses
class UserAddress(models.Model):
	house_number = models.CharField(max_length=10)
	street = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=10)
	country = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=20, decimal_places=6, null=True, blank=True)
	# class Meta:
	# 	db_table = 'django_blog_useraddress'

class Progress(models.Model):
    name = models.CharField(max_length=30)
    Jan_2023 = models.PositiveIntegerField(default=0)
    April_2023 = models.PositiveIntegerField(default=0)
    August_2023 = models.PositiveIntegerField(default=0)
    December_2023 = models.PositiveIntegerField(default=0)
    April_2024 = models.PositiveIntegerField(default=0)