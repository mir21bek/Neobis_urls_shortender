from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

import random

from .models import UrlShortener


@api_view(["POST"])
def make_short_url(request):
    data = request.data
    longer = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    short_url = ("".join(random.sample(longer, 6)))
    UrlShortener.objects.create(
        long_url = data['long_url'],
        short_url=short_url
    )
    long_url = data['long_url']
    short_url = "http://localhost:8000/"+short_url
    return Response({'long_url': long_url, 'short_url': short_url})


def redirect_url(request, short_url):
    try:
        obj = UrlShortener.objects.get(short_url=short_url)
    except UrlShortener.DoesNotExist:
        obj = None
    if obj is not None:
        return redirect(obj.long_url)

