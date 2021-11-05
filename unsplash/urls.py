from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('unsplash_index',views.index,name="index"),
    path('genrate_image',views.getImage,name="getImange"),
    path('linkedin_cover',views.linkedin_cover,name="linkedin_cover"),
    path('twitter_cover',views.twitter_cover,name="twitter_cover"),
    path('facebook_cover',views.facebook_cover,name="facebook_cover"),
    # path('getpic',views.getpic,name="getpic"),
]