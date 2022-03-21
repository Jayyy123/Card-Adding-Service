from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
]