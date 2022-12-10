from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = "comment"

urlpatterns = [
    path("", views.CommentsListView.as_view(), name="comment-list"),
    path("<int:pk>/", views.CommentDetailView.as_view(), name="comment-detail"),
    path("create/", views.CommentCreateView.as_view(), name="create-comment"),
    path("<int:pk>/edit/", views.CommentEditView.as_view(), name="post-edit"),
    path("<int:pk>/delete/",views.CommentDeleteView.as_view(),name="post-delete"),
   
    path("api/v1/", include("comment.api.v1.urls")),
]
