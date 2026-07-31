from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")
    pk_url_kwarg = "post_id"

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("post_list")
    pk_url_kwarg = "post_id"