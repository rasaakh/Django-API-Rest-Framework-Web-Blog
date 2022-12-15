from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from comment.forms import CommentForm
from comment.models import Comment
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator


class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["posts"] = Post.objects.all()
        return context


class PostListView(LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    queryset = Post.objects.all()
    # model = Post
    context_object_name = "posts"
    # paginate_by = 1
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content','status', 'category', 'published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        profile = Profile.objects.get(user_id=self.request.user.id)
        form.instance.author = profile
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"


def blog_single(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Your comment was successfully registered"
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Your comment was Not successfully "
            )

    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    post = get_object_or_404(posts, pk=pid)

    post.counted_view += 1
    post.save()
    pos = Paginator(posts, 1)
    pos = pos.get_page(pid)

    if post.login_required is False or request.user.is_authenticated:
        comments = Comment.objects.filter(post=post.id, approved=True)
        form = CommentForm()
        context = {"post": post, "comments": comments, "form": form}
        return render(request, "blog-single.html", context)
    else:
        return HttpResponseRedirect(reverse("accounts:login"))


def blog_search(request):

    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    if request.method == "GET":
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    context = {"posts": posts}
    return render(request, "post_list_search.html", context)
