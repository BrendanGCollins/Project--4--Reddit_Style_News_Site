from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Display list of all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


# Display details of a specific post, including comments
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(
        request, 'posts/post_detail.html',
        {
            'post': post,
            'form': form,
            'comments': comments
        }
    )


# Create a new post
@login_required(login_url='login')
def create_post(request):
    # Add an informational message if the user is not authenticated
    if not request.user.is_authenticated:
        messages.info(
            request,
            "You need to be logged in to create a post. "
            "Please log in or register."
        )

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Add a success message after creating the post
            messages.success(
                request, "Your post has been created successfully!"
            )
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


# Update an existing post
@login_required(login_url='login')
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Ensure that only the author can edit their post
    if request.user != post.author:
        messages.error(
            request,
            "You do not have permission to edit this post."
        )
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your post has been updated successfully."
            )
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(
        request, 'posts/update_post.html', {'form': form, 'post': post}
    )


# Delete an existing post
@login_required(login_url='login')
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Ensure that only the author can delete their post
    if request.user != post.author:
        messages.error(
            request,
            "You do not have permission to delete this post."
        )
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "The post has been deleted successfully.")
        return redirect('home')

    return render(request, 'posts/delete_post.html', {'post': post})


# Upvote a post
@login_required(login_url='login')
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.add(request.user)
        messages.success(request, "You have successfully upvoted this post.")
    else:
        messages.info(request, "You have already upvoted this post.")
    return redirect('post_detail', post_id=post_id)


# Upvote a comment
@login_required(login_url='login')
def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.upvotes.filter(id=request.user.id).exists():
        comment.upvotes.add(request.user)
        messages.success(
            request,
            "You have successfully upvoted this comment."
        )
    else:
        messages.info(
            request,
            "You have already upvoted this comment."
        )
    return redirect('post_detail', post_id=comment.post.id)
