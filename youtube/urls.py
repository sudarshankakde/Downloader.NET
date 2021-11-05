from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('youtube_index',views.index,name='index'),
    path('data',views.data , name='data'),
    path('data_download',views.data_download , name='data_download'),
]
