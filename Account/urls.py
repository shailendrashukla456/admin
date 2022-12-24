from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout')
]
