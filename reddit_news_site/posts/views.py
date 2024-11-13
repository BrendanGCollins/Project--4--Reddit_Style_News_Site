from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

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

    return render(request, 'posts/post_detail.html', {'post': post, 'form': form, 'comments': comments})