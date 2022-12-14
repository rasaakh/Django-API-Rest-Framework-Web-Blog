from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from comment.models import Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentsListView(ListView):
    permission_required = "blog.view_post"
    queryset = Comment.objects.all()

    context_object_name = "comment"
    # paginate_by = 1
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class CommentDetailView(LoginRequiredMixin, DetailView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment

    form_class = CommentForm
    success_url = "/comment/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentEditView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = "/comment/"


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = "/comment/"
