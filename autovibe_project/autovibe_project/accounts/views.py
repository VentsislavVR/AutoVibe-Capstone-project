from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views

from autovibe_project.accounts.forms import AutoVibeUserCreationForm


# Create your views here.
class RegisterUserView(views.CreateView):
    template_name = "accounts/register_user.html"
    form_class = AutoVibeUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_user.html"
    redirect_authenticated_user = True
#Todo figure this out
class LogoutUserView(auth_views.LogoutView):
    template_name = "accounts/logout_user.html"
    http_method_names = ["get", "post"]

# def logout_user(request):
#
#     logout(request)
#     return redirect('index')






class ProfileDetailsView():
    ...
class ProfileUpdateView():
    ...

class ProfileDeleteView():
    ...