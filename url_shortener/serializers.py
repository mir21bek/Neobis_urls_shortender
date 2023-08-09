from rest_framework.serializers import ModelSerializer
from .models import UrlShortener


class UrlShortenerSerializers(ModelSerializer):
    model = UrlShortener
    fields = ['long_url', 'short_url']
