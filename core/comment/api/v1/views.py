from comment.models import Comment
from .serializers import CommentUpdateCreateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentUpdateCreateSerializer
    queryset = Comment.objects.filter(approved=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'category':["exact","in"], 'author':["exact"],'status':["exact"]}
    # filterset_class = PostFilters
    search_fields = ["name", "message"]
    ordering_fields = ["created_date"]
    # pagination_class = DefaultPagination
