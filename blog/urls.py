from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),

    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),

    path("create/", views.PostCreateView.as_view(), name="create_post"),

    path("edit/<int:post_id>/",
         views.PostUpdateView.as_view(),
         name="edit_post"),

    path("delete/<int:post_id>/",
         views.PostDeleteView.as_view(),
         name="delete_post"),
]