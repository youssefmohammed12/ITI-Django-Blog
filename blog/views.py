from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts
    })


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {
        "form": form
    })


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm(instance=post)

    return render(request, "blog/edit_post.html", {
        "form": form,
        "post": post
    })


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "blog/delete_post.html", {
        "post": post
    })