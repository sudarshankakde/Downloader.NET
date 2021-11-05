from django.shortcuts import render
from . import models
import random2

urllist = [
   'https://source.unsplash.com/random',
   "https://source.unsplash.com/collection/190727/1600x900",
   'https://source.unsplash.com/daily',
   'https://source.unsplash.com/weekly?nature',
   'https://source.unsplash.com/featured/?world,dark'
]
# Create your views here.
def index(request):
   url= 'https://source.unsplash.com/random'
   return render(request, 'unsplash_index.html',{'image':url})



def getImage(request):
   key = str(request.GET['key'])
   size1 = request.GET['sceensize']
   url = 'https://source.unsplash.com/'
   url = url+str(size1)+'/?'+key
   return render(request, 'unsplash_index.html',{'image':url,'key':key})

def linkedin_cover(request):
   url= 'https://source.unsplash.com/800x200/?work,student'
   return render(request, 'cover_templet.html',{'cover_name':'Linkedin Cover','url':url})


def twitter_cover(request):
   url= 'https://source.unsplash.com/1500x500/?work,student'
   return render(request, 'cover_templet.html',{'cover_name':'Twitter Cover','url':url})


def facebook_cover(request):
   url= 'https://source.unsplash.com/851x315/?work,student'
   return render(request, 'cover_templet.html',{'cover_name':'Facebook Cover','url':url})