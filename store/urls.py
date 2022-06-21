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
    path('recent',views.recent_file),
    path('download',views.download_file),
    path('trashfiles',views.trash_files),
    path('del',views.trash),
    path('updatepic',views.profile),
    path('allfile',views.all_file),
    path('setsize',views.setsize),
    path('typesize',views.typesize)
]