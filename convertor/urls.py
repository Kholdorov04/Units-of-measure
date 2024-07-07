from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('convert_length/', views.convert_length, name='convert_length'),
    path('convert_weight/', views.convert_weight, name='convert_weight'),
]