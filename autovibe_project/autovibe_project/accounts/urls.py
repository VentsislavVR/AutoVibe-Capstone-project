from django.urls import path, include

from autovibe_project.accounts import views

urlpatterns = (

    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', views.LogoutUserView.as_view(), name='logout_user'),
    #
    # path('profile/<int:pk>/',include([
    #     path('', views.ProfileDetailsView.as_view(), name='profile_details'),
    #     path('update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    #     path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
    # ])),

)