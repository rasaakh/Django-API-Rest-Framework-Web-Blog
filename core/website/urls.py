from django.urls import path
from . import views


app_name = "website"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostListApiView.as_view(), name="post-list-web"),
    # path("post/", views.PostListView.as_view(), name="post-list"),
    # path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]
