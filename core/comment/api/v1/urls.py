from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "comment-api-v1"

router = DefaultRouter()
router.register("comment", views.CommentModelViewSet, basename="comment")
urlpatterns = router.urls


# urlpatterns = [
#     path("", CommentsList.as_view(), name="list"),
#     path("<int:pk>/", CommentsDetail.as_view(), name="detail"),
#     path("create/", CommentCreate.as_view(), name="create"),
#     path("update-delete/<int:pk>/", CommentUpdateDelete.as_view(), name="update-delete"),
# ]
