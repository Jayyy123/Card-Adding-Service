from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('about/', views.base, name='about'),
    path('contact/', views.base, name='contact'),
]