"""
URL configuration for autovibe_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from autovibe_project.common.views import Error404View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('autovibe_project.home.urls')),
    path('accounts/',include('autovibe_project.accounts.urls')),
    path('common/',include('autovibe_project.common.urls')),
    path('carpost/',include('autovibe_project.carpost.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = Error404View.as_view()
