from django.urls import path 
from . import views

urlpatterns = [
    path('upload', views.upload),
    path('otpverify',views.otpverify),
    path('register', views.register),
    path('login',views.log_in),
    path('logout',views.out),
    path('getfiles',views.files),
    path('dashboard',views.details),
    path('files',views.files),
    path('folder',views.fold),
    path('addfolder',views.addfolder),
    path('recent',views.recent_file)
]