from django.urls import path
from . import views

urlpatterns = [
    # List all posts (homepage)
    path('', views.post_list, name='home'),

    # View post details
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Create a new post
    path('post/new/', views.create_post, name='create_post'),

    # Edit a post
    path('post/<int:post_id>/edit/', views.update_post, name='update_post'),

    # Delete a post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),

    # Upvote a post
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),

    # Upvote a comment
    path(
        'comment/<int:comment_id>/upvote/',
        views.upvote_comment,
        name='upvote_comment',
    ),
]
