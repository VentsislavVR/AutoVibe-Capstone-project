from django.contrib import admin

from autovibe_project.cars.models import CarPost, CarBrand, CarFeaturePost


class CarFeatureInline(admin.StackedInline):
    model = CarFeaturePost
# Register your models here.
@admin.register(CarPost)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price', 'mileage', 'vin', 'description')
    list_filter = ('brand', 'model', 'year', 'color', 'price', 'mileage', 'vin', 'description')
    search_fields = ('brand', 'model', 'year', 'color', 'price', 'mileage', 'vin', 'description')
    inlines = [CarFeatureInline]
@admin.register(CarBrand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'country_of_origin', 'logo')
    list_filter = ('brand_name', 'country_of_origin', 'logo')
    search_fields = ('brand_name', 'country_of_origin', 'logo')
