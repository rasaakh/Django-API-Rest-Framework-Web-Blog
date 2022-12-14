# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login

# from accounts.models import User
from django.shortcuts import redirect

# from django.views.generic import TemplateView

# Create your views here.
from django.contrib.auth import get_user_model

# from django.shortcuts import redirect
from .forms import SignUpForm


User = get_user_model()


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("blog:post-list")

    class Meta:
        model = User


class RegisterPage(FormView):
    template_name = "accounts/register.html"

    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("blog:post-list")

    class Meta:
        model = User

        fields = ("email", "password1", "password2")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("blog:post-list")
        return super(RegisterPage, self).get(*args, **kwargs)
