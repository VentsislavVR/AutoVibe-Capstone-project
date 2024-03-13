# import os
# import django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autovibe_project.settings")
# django.setup()
#
# from autovibe_project.carpost.models import CarModel, CarBrands
#
# # Populate the CarBrands table if needed
# # for brand_code, brand_name in CarBrands.BRAND_CHOICES:
# #     CarBrands.objects.get_or_create(brand_name=brand_name)
#
# # Populate the CarModel table
# for brand_name, models in CarModel.TEN_POPULAR_MODELS_PER_BRAND.items():
#     brand = CarBrands.objects.get(brand_name=brand_name)
#     for model_name in models:
#         CarModel.objects.get_or_create(brand=brand, name=model_name)
#
# print("CarModel populated successfully.")
