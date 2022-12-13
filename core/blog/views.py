from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from .models import Post
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


class IndexView(TemplateView):
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context["posts"] = Post.objects.all()
        return context





class PostListView(LoginRequiredMixin,ListView):
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
