from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from django.utils.translation import gettext_lazy as _

from autovibe_project.accounts.forms import AutoVibeUserCreationForm, ProfileUpdateForm
from autovibe_project.accounts.models import Profile


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

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs['placeholder'] = _('Email')
        form.fields['password'].widget.attrs['placeholder'] = _('Password')
        return form
#Todo figure this out
class LogoutUserView(auth_views.LogoutView):
    template_name = "accounts/logout_user.html"
    http_method_names = ["get", "post"]

# def logout_user(request):
#
#     logout(request)
#     return redirect('index')






class ProfileDetailsView(auth_mixins.LoginRequiredMixin,views.DetailView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'accounts/details_profile.html'

class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'accounts/edit_profile.html'
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(views.DeleteView):
    ...