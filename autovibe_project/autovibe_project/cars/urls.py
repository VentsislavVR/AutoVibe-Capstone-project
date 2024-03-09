from django.urls import path


from autovibe_project.cars.views import CreateCarPostView

urlpatterns = (
    path('create/', CreateCarPostView.as_view(), name='create_car_post'),


)