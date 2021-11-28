from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('signup', views.signUp, name="signup"),
    path('signIn', views.signIn, name="login"),
    path('signout', views.signOut, name="signout"),
    path('signout', views.signOut, name="signout"),
]
