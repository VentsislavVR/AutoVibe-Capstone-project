from django.urls import path, include

from autovibe_project.articles import views

urlpatterns = (
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    path('create/', views.ArticlesCreateView.as_view(), name='article_create'),
    path('<int:pk>/<slug:slug>/',include(
        [
            path('', views.ArticlesDetailView.as_view(), name='article_details'),
            path('update/', views.ArticlesUpdateView.as_view(), name='article_update'),
            path('delete/', views.ArticlesDeleteView.as_view(), name='article_delete'),
        ]
    ))
)