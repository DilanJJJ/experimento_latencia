from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health-check/', views.healthCheck),
    path('api/ingesta/', include('ingesta_datos.urls')),
    path('api/procesamiento/', include('procesamiento.urls')),
]