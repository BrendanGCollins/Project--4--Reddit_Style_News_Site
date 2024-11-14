from django.contrib import admin
from .models import Category, Post, Comment, UserProfile

# Register your models here.
admin.site.register(Category)  # Register Category model to add/edit categories in the admin
admin.site.register(Post)      # Register Post model to add/edit posts
admin.site.register(Comment)   # Register Comment model to add/edit comments on posts
admin.site.register(UserProfile)  # Register UserProfile model to manage user profiles