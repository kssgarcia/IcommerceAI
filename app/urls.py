from django.urls import path 
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='page-home'),
    path('login/', views.Login.as_view(), name='page-login'),
    path('register/', views.Register.as_view(), name='page-register'),
    path('logout/', LogoutView.as_view(next_page="page-home"), name="page-logout"),
    path('password/', views.PasswordsChangeView.as_view(), name="page-password-change"),
]

