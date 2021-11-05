from django.shortcuts import render
import os
from typing import Counter
import pytube
from pytube.request import stream
from .models import stream_data

# index
def index(request):
    return render(request,'youtube_index.html')

def data(request):
    global url
    url = request.POST['link']
    yt = pytube.YouTube(url)
    stream1 = stream_data()
    stream1.higest = yt.streams.get_highest_resolution()
    stream1.title = yt.title
    stream1.thubnail = yt.thumbnail_url
    return render(request , 'youtube_streams.html', {'stream1':stream1})



def data_download(request):
    yt = pytube.YouTube(url)
    choices = request.POST['choice']
    if choices== 'heightResolution':
        stream = yt.streams.get_highest_resolution()
        stream.download()
    elif choices == 'lowestResolution':
        stream = yt.streams.get_lowest_resolution()
        stream.download()
    elif choices == 'audioOnly':
        stream = yt.streams.get_audio_only()
        stream.download()
    else:
        pass
    return render(request,'youtube_downloaded.html')

