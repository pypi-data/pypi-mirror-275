from django.contrib import admin
from .models import Post, UserAddress


# Register the Post and UserAddress models with the Django admin site
admin.site.register(Post)
admin.site.register(UserAddress)
