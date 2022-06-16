from django.urls import path 
from . import views

urlpatterns = [
    path('upload', views.upload),
    path('register', views.register),
    path('login',views.log_in),
    path('logout',views.out)
]