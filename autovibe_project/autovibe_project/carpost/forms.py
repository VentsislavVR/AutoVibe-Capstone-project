from django import forms

from autovibe_project.carpost.models import CarModel, CarPost, CarFeatures




class CarBrandModelForm(forms.ModelForm):
    brand = forms.ChoiceField(choices=[(brand, brand) for brand in CarModel.TEN_POPULAR_MODELS_PER_BRAND.keys()])
    model = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brand = self.data.get('0-brand')  # Assuming '0-brand' is the key for the brand data in kwargs
        model = self.data.get('0-model')  # Assuming '0-model' is the key for the model data in kwargs

        self.fields['brand'].widget.attrs.update({'onchange': 'this.form.submit();'})

        if brand:
            self.fields['brand'].initial = brand
            self.fields['model'].choices = [(model, model) for model in
                                            CarModel.TEN_POPULAR_MODELS_PER_BRAND.get(brand, [])]

    def clean(self):
        cleaned_data = super().clean()
        brand = cleaned_data.get('brand')
        model = self.data.get('0-model')
        if brand:
            models_for_brand = CarModel.TEN_POPULAR_MODELS_PER_BRAND.get(brand, [])
            self.fields['model'].choices = [(model, model) for model in models_for_brand]
            if model not in models_for_brand:
                self.add_error('model', 'Invalid model selected.')
        return cleaned_data
    class Meta:
        model = CarModel
        fields = ['brand', 'model']

class CarPostForm(forms.ModelForm):
    class Meta:
        model = CarPost
        fields = ['municipality', 'year', 'color', 'engine', 'horsepower', 'transmission', 'chassis', 'price', 'mileage', 'vin', 'description', 'image']

    def __init__(self, *args, **kwargs):
        brand = kwargs.pop('brand', None)
        model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
        if brand:
            # Set initial value for brand field
            self.fields['brand'].initial = brand
            # Disable brand field to prevent changes
            self.fields['brand'].widget.attrs['disabled'] = True
        if model:
            # Set initial value for model field
            self.fields['model'].initial = model
            # Disable model field to prevent changes
            self.fields['model'].widget.attrs['disabled'] = True
class CarFeaturesForm(forms.ModelForm):
    class Meta:
        model = CarFeatures
        fields = ['interior_features', 'exterior_features', 'safety_features', 'other_features']
        widgets = {
            'interior_features': forms.CheckboxSelectMultiple,
            'exterior_features': forms.CheckboxSelectMultiple,
            'safety_features': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interior_features'].choices = CarFeatures.INTERIOR_FEATURES_CHOICES
        self.fields['exterior_features'].choices = CarFeatures.EXTERIOR_FEATURES_CHOICES
        self.fields['safety_features'].choices = CarFeatures.SAFETY_FEATURES_CHOICES