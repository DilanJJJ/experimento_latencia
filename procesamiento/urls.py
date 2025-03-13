from django.urls import path
from . import views

urlpatterns = [
    path('procesar/<int:archivo_id>/', views.procesar_archivo, name='procesar_archivo'),
]