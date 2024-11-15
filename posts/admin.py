from django.contrib import admin
from .models import Category, Post, Comment, UserProfile

# Register your models here.
admin.site.register(Category)  # Register Category model for admin
admin.site.register(Post)      # Register Post model for admin
admin.site.register(Comment)   # Register Comment model for admin
admin.site.register(UserProfile)  # Register UserProfile model for admin
