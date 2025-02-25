from django.db import models
from django.contrib.auth.models import User


# Category model for grouping posts into categories
class Category(models.Model):
    # Category name
    name = models.CharField(max_length=255)

    def __str__(self):
        # Return category name as string representation
        return self.name


# Post model representing a news post
class Post(models.Model):
    # Post title
    title = models.CharField(max_length=255)

    # Post content
    content = models.TextField()

    # Link to author (User)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Optional category
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    # Auto-populated timestamp for creation
    created_at = models.DateTimeField(auto_now_add=True)

    # Auto-updated timestamp for modifications
    updated_at = models.DateTimeField(auto_now=True)

    # Track users who upvoted
    upvotes = models.ManyToManyField(
        User, related_name='post_upvotes', blank=True
    )

    def __str__(self):
        # Return post title as string representation
        return self.title

    def upvote_count(self):
        # Return count of upvotes
        return self.upvotes.count()

    def upvote(self, user):
        # Add user to upvotes if they haven't already upvoted
        if not self.upvotes.filter(id=user.id).exists():
            self.upvotes.add(user)


# Comment model representing comments on posts
class Comment(models.Model):
    # Link to post
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )

    # Link to author (User)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Comment content
    content = models.TextField()

    # Timestamp for creation
    created_at = models.DateTimeField(auto_now_add=True)
     
    # New: Allow replies to be stored but remove parent link if a parent comment is deleted
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='replies'
    )

    # Track users who upvoted
    upvotes = models.ManyToManyField(
        User, related_name='comment_upvotes', blank=True
    )

    def __str__(self):
        # String representation
        return f'Comment by {self.author.username} on {self.post.title}'

    def upvote_count(self):
        # Return count of upvotes
        return self.upvotes.count()

    def upvote(self, user):
        # Add user to upvotes if they haven't already upvoted
        if not self.upvotes.filter(id=user.id).exists():
            self.upvotes.add(user)


# UserProfile model extending the default User model to add more fields
class UserProfile(models.Model):
    # Link to default Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Optional bio field
    bio = models.TextField(blank=True)

    # Optional avatar image
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Optional personal website link
    website = models.URLField(blank=True)

    def __str__(self):
        # String representation
        return f'Profile of {self.user.username}'
