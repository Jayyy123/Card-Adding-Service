from django.urls import path
from . import views

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('login_page/', views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('account/', views.account, name='account'),
]