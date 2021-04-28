from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import Songserializer
from .models import Song
from .serializer import Podcastserializer
from .models import Podacst
from .serializer import Audiobookserializer
from .models import Audiobook

# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls = {
    'List': '/Song-list/<int:id>',
    'Detail view': '/Song-detail',
    'Create': '/Song-Create',
    'Update': '/Song-Update/<int:id>',
    'Delete': '/Song-Delete/<int:id>',


    }

    return Response(api_urls);

@api_view(['GET'])
def showall(request):
    Song = Song.objects.all()
    serializer = Songserializer(Song, many=True)
    returm Response(serializer.date)

@api_view(['GET'])
def showall(request):
    Podacst = Podcast.objects.all()
    serializer = Podcastserializer(Podcast, many=True)
    returm Response(serializer.date)

@api_view(['POST'])
def showall(request):
    Audiobook = Audiobook.objects.all()
    serializer = Audiobookserializer(Audiobook, many=True)
    returm Response(serializer.date)
