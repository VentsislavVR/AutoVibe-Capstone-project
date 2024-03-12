from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from autovibe_project.cars.forms import CarMultiForm, CarFeaturePostForm, CarBrandForm, CarPostForm
from autovibe_project.cars.models import CarPost, CarFeaturePost, CarBrand

UserModel = get_user_model()


class CreateCarPostView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = CarPost
    form_class = CarMultiForm
    template_name = 'cars/create_car_post.html'
    def get_success_url(self):
        return reverse_lazy('details_car', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_brand_form'] = CarBrandForm()
        context['form'] = CarPostForm()
        context['car_feature_form'] = CarFeaturePostForm()

        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()


        return super().form_valid(form)
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)


class DetailsCarView(views.DetailView):
    model = CarPost
    template_name = 'cars/details_car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UpdateCarView(views.UpdateView):
    pass


class DeleteCarView(views.DeleteView):
    pass
