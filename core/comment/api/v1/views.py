from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from blog.models import Post
from comment.models import Comment
from .serializers import (
    CommentListSerializer,
    CommentUpdateCreateSerializer,
)

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)
from rest_framework import viewsets
from .serializers import CommentUpdateCreateSerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# class CommentsList(APIView):
#     """
#     get:
#         Returns the list of comments on a particular post.

#         parameters = [pk]
#     """

#     def get(self, request):
        
#         query = Comment.objects.all()
#         serializer = CommentListSerializer(query, many=True)
#         return Response(
#             serializer.data, 
#             status=status.HTTP_200_OK,
#         )

# class CommentsDetail(APIView):
#     """
#     get:
#         Returns the list of comments on a particular post.

#         parameters = [pk]
#     """

#     def get(self, request, pk):
#         post = get_object_or_404(Post, id=pk, status="p")
#         query = Comment.objects.filter_by_instance(post)
#         serializer = CommentListSerializer(query, many=True)
#         return Response(
#             serializer.data, 
#             status=status.HTTP_200_OK,
#         )



# class CommentCreate(APIView):
#     """
#     post:
#         Create a comment instnace. Returns created comment data.

#         parameters: [object_id, name, parent, body,]
#     """

#     permission_classes = [IsAuthenticated,]

#     def post(self, request):
#         serializer = CommentUpdateCreateSerializer(data=request.data)
        
#         if serializer.is_valid():
#             post = get_object_or_404(Post, pk=serializer.data.get('object_id'))
#             # comment_for_model = ContentType.objects.get_for_model(post)
#             comment = Comment.objects.create(
#                 # user = request.user,
#                 post = serializer.data.get('post'),
#                 name = serializer.data.get('name'),
#                 email=serializer.data.get('email'),
#                 # content_type = comment_for_model,
#                 # object_id = post.id,
#                 subject = serializer.data.get('subject'),
#                 message = serializer.data.get('message'),
#                 approaed= serializer.data.get('approaed')
#             )
#             return Response(
#                 serializer.data, 
#                 status=status.HTTP_201_CREATED,
#             )
        
#         else:
#             return Response(
#                 serializer.errors, 
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
            

# class CommentUpdateDelete(APIView):
#     """
#     put:
#         Updates an existing comment. Returns updated comment data.

#         parameters: [object_id, name, parent, body,]

#     delete:
#         Delete an existing comment.

#         parameters: [pk]
#     """

#     permission_classes = [IsAuthenticated,]

#     def put(self, request, pk):
#         comment = get_object_or_404(Comment, pk=pk, user=request.user)
#         serializer = CommentUpdateCreateSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data, 
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 serializer.errors, 
#                 status=status.HTTP_400_BAD_REQUEST,
#             )


#     def delete(self, request, pk):
#         comment = get_object_or_404(Comment, pk=pk, user=request.user)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT,)



class CommentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class =CommentUpdateCreateSerializer
    queryset = Comment.objects.filter(approved=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'category':["exact","in"], 'author':["exact"],'status':["exact"]}
    # filterset_class = PostFilters
    search_fields = ["name", "message"]
    ordering_fields = ["created_date"]
    # pagination_class = DefaultPagination