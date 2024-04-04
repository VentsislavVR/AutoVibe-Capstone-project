
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
    path('articles/',include('autovibe_project.articles.urls')),
    path('merchshop/',include('autovibe_project.merchshop.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = Error404View.as_view()
