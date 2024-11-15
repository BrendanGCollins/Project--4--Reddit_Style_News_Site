from django.db import models
from django.contrib.auth.models import User

# Category model for grouping posts into categories
class Category(models.Model):
    name = models.CharField(max_length=255)  # Category name

    def __str__(self):
        return self.name  # Return category name as string representation

# Post model representing a news post
class Post(models.Model):
    title = models.CharField(max_length=255)  # Post title
    content = models.TextField()  # Post content
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to author (User)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Optional category
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-populated timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updated timestamp for modifications
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True)  # Track users who upvoted

    def __str__(self):
        return self.title  # Return post title as string representation

    def upvote_count(self):
        return self.upvotes.count()  # Return count of upvotes

    def upvote(self, user):
        if not self.upvotes.filter(id=user.id).exists():
            self.upvotes.add(user)  # Add user to upvotes if they haven't already upvoted

# Comment model representing comments on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to author (User)
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)  # Track users who upvoted

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'  # String representation

    def upvote_count(self):
        return self.upvotes.count()  # Return count of upvotes

    def upvote(self, user):
        if not self.upvotes.filter(id=user.id).exists():
            self.upvotes.add(user)  # Add user to upvotes if they haven't already upvoted

# UserProfile model extending the default User model to add more fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to default Django User
    bio = models.TextField(blank=True)  # Optional bio field
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Optional avatar image
    website = models.URLField(blank=True)  # Optional personal website link

    def __str__(self):
        return f'Profile of {self.user.username}'  # String representation