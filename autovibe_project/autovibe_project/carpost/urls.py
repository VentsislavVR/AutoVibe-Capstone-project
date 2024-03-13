from django.urls import path, include

from autovibe_project.carpost.views import CreateCarPostWizardView, DetailsCarView, UpdateCarView, DeleteCarView, \
    CarPostListView

urlpatterns = (
    path('posts', CarPostListView.as_view(), name='list_car_post'),
    path('create/', CreateCarPostWizardView.as_view(), name='create_car_post'),
    path('<int:pk>/', include([
        path('', DetailsCarView.as_view(), name='details_car_post'),
        path('update/',UpdateCarView.as_view(), name='update_car_post'),
        path('delete/',DeleteCarView.as_view(), name='delete_car_post'),

    ]))

)