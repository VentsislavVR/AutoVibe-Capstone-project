from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from autovibe_project.cars.forms import CarPostForm, UserProfileMultiForm, CarFeaturePostForm, CarBrandForm
from autovibe_project.cars.models import CarPost, CarFeaturePost, CarBrand

UserModel = get_user_model()


class CreateCarPostView(views.CreateView):
    model = CarPost
    template_name = 'cars/create_car_post.html'
    form_class = CarPostForm  # Use CarPostForm for creating CarPost instance
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_feature_form'] = CarFeaturePostForm()  # Add CarFeaturePostForm to the context
        context['car_brand_form'] = CarBrandForm()  # Add CarBrandForm to the context
        return context

    def form_valid(self, form):
        car_feature_form = CarFeaturePostForm(self.request.POST)  # Initialize CarFeaturePostForm with POST data
        car_brand_form = CarBrandForm(self.request.POST)  # Initialize CarBrandForm with POST data

        if car_feature_form.is_valid() and car_brand_form.is_valid():
            self.object = form.save(commit=False)  # Save the CarPost instance
            self.object.profile = self.request.user.profile  # Associate CarPost with current user's profile

            # Get the brand name from the form data and fetch or create the Brand instance
            brand_name = car_brand_form.cleaned_data['brand_name']
            brand_instance, _ = CarBrand.objects.get_or_create(brand_name=brand_name)
            self.object.brand = brand_instance  # Associate CarPost with Brand instance

            self.object.save()

            car_feature = car_feature_form.save(commit=False)
            car_feature.car = self.object  # Associate CarFeaturePost with CarPost instance
            car_feature.save()

            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, car_feature_form=car_feature_form, car_brand_form=car_brand_form))


