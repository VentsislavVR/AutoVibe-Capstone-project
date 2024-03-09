from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from autovibe_project.cars.models import CarBrand, CarPost, CarFeaturePost
from betterforms.multiform import MultiModelForm

# class CarForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['year'].widget.attrs['placeholder'] = 'Product Year'
#         self.fields['color'].widget.attrs['placeholder'] = 'Color'
#         self.fields['model'].widget.attrs['placeholder'] = 'Model'
#         self.fields['price'].widget.attrs['placeholder'] = 'Price'
#         self.fields['mileage'].widget.attrs['placeholder'] = 'Mileage'
#         self.fields['vin'].widget.attrs['placeholder'] = 'Vin'
#         self.fields['description'].widget.attrs['placeholder'] = 'Description'
#
#     def clean_year(self):
#         year = self.cleaned_data.get('year')
#         current_year = timezone.now().year
#         if year and year > current_year + 1:
#             raise ValidationError("Year should not be greater than the current year plus one.")
#         return year
#     class Meta:
#         model = CarPost
#         fields = '__all__'
#
# class CarBrandForm(forms.ModelForm):
#
#     class Meta:
#         model = CarBrand
#         fields = '__all__'
#
# class CarFeatureForm(forms.ModelForm):
#
#
#     class Meta:
#         model = CarFeaturePost
#         fields = '__all__'
#
#         widgets = {
#             'interior_features': forms.CheckboxSelectMultiple,
#             'exterior_features': forms.CheckboxSelectMultiple,
#             'safety_features': forms.CheckboxSelectMultiple,
#         }
#
class CarBrandForm(forms.ModelForm):

    class Meta:
        model = CarBrand
        fields = ['brand_name']
class CarPostForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['model', 'year', 'color', 'price', 'mileage', 'vin', 'description', 'image']

class CarFeaturePostForm(forms.ModelForm):
    class Meta:
        model = CarFeaturePost
        fields = ['interior_features', 'exterior_features', 'safety_features', 'other_features']

class UserProfileMultiForm(MultiModelForm):
    form_classes = {
        'form': CarPostForm,
        'carfeaturepost': CarFeaturePostForm,
        'brand_name': CarBrandForm
    }