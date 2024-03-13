from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from formtools.wizard.views import SessionWizardView
from django.contrib.auth import mixins as auth_mixins

from autovibe_project.carpost.forms import CarBrandModelForm, CarPostForm, CarFeaturesForm
from autovibe_project.carpost.models import CarModel, CarPost


#Todo maybe add xondition for 3rd form

class CreateCarPostWizardView(auth_mixins.LoginRequiredMixin,SessionWizardView):
    template_name = 'cars/create_car_post.html'
    file_storage = FileSystemStorage(location='/mediafiles/car_images')
    form_list = [
        CarBrandModelForm,
        CarPostForm,
        CarFeaturesForm,

    ]
    # def get_success_url(self):
    #     return reverse_lazy('details_car_post',
    #                         kwargs={'pk': self.object.pk})

    def get_form_instance(self, step):
        if step == 'car_brand_model':
            return self.initial.get('car_brand_model', {})
        elif step == 'car_post':
            return self.initial.get('car_post', {})
        elif step == 'car_features':
            return self.initial.get('car_features', {})
        return None

    def done(self, form_list, **kwargs):
        car_brand_model_data = form_list[0].cleaned_data
        car_post_data = form_list[1].cleaned_data
        car_features_data = form_list[2].cleaned_data

        brand = car_brand_model_data.get('brand')
        model = car_brand_model_data.get('model')

        car_model_instance, created = CarModel.objects.get_or_create(brand=brand, model=model)

        car_post = form_list[1].save(commit=False)
        car_post.user = self.request.user
        car_post.car_model = car_model_instance
        car_post.save()

        car_features = form_list[2].save()
        car_features.save()

        car_post.car_feature.add(car_features)
        print(car_post.car_feature.set)

        return redirect('details_car_post', pk=car_post.pk)


class CarPostListView(views.ListView):
    queryset = CarPost.objects.all()\
        .prefetch_related('car_feature', 'car_model')

    template_name = 'cars/list_car.html'
    # paginate_by = 10



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q') or ''

        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(car_model__brand__icontains=query) |
                Q(car_model__model__icontains=query) |
                Q(year__icontains=query) |
                Q(price__icontains=query)
            )

        return queryset


class DetailsCarView(views.DetailView):
    template_name = 'cars/details_car.html'
    model = CarPost

    def get_queryset(self):
        return super().get_queryset().prefetch_related('car_feature', 'car_model')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        car_post = self.object
        car_features = car_post.car_feature.all()
        brand = car_post.car_model.brand
        model = car_post.car_model.model

        features = {
            'interior': [],
            'exterior': [],
            'safety': [],
            'other': []
        }

        for feature in car_features:
            features['interior'].extend(feature.interior_features)
            features['exterior'].extend(feature.exterior_features)
            features['safety'].extend(feature.safety_features)
            features['other'].append(feature.other_features)

        context['brand'] = brand
        context['model'] = model
        context['features'] = features

        return context


class UpdateCarView(views.UpdateView):
    pass


class DeleteCarView(views.DeleteView):
    pass