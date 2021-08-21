from django.contrib import admin
from django.urls import path, include
from bakersoft.views import home, ProduktAPI,ProdukteAPI
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api', ProdukteAPI.as_view()),
    path('api/<int:produkt_id>/', ProduktAPI.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
