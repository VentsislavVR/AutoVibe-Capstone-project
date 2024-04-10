from django.contrib import admin
from autovibe_project.carpost.models import CarBrands, CarModel, CarPost, CarFeatures

@admin.register(CarBrands)
class CarBrandsAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model')
    search_fields = ('brand', 'model')

@admin.register(CarFeatures)
class CarFeaturesAdmin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(CarPost)
class CarPostAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'year', 'color', 'price')
    list_filter = ('year', 'color', 'price')
    search_fields = ('car_model__brand', 'car_model__model')
    autocomplete_fields = ['car_model']