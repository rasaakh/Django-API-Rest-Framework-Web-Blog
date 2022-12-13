from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "website"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.PostListApiView.as_view(), name="post-list-web"),
    # path("post/", views.PostListView.as_view(), name="post-list"),
   
    # path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
 
]
