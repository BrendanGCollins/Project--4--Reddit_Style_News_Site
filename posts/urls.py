from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),  # List all posts (homepage)
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # View post details
    path('post/new/', views.create_post, name='create_post'),  # Create a new post
    path('post/<int:post_id>/edit/', views.update_post, name='update_post'),  # Edit a post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Delete a post
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),  # Upvote a post
    path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),  # Upvote a comment
]