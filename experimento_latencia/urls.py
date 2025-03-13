from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ingesta/', include('ingesta_datos.urls')),
    path('api/procesamiento/', include('procesamiento.urls')),
]