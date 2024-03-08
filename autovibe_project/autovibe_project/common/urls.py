
from django.urls import path

from autovibe_project.common import views

urlpatterns = (
    path('about/', views.AboutView.as_view(), name='about_page'),
)