from django.urls import path, include
from . import views
from .views import blog_single, blog_search

app_name = "blog"

urlpatterns = [
    path("post/", views.PostListView.as_view(), name="post-list"),
    # path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pid>/", blog_single, name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    path("search/", blog_search, name="search"),
]
