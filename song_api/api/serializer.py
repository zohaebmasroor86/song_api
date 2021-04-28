from rest_framework import serializer

from models import Song
from models import Podcast
from models import Audiobook

class Songserializer(serializer.Modelserializer)
class Podcastserializer(serializer.Modelserializer)
class Audiobookserializer(serializer.Modelserializer)

class Meta:
    model = 'Song', 'Podcast', 'Audiobook'
    field = '__all__'
