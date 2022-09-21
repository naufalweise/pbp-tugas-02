from django.http import HttpResponse
from .models import MyWatchList
from django.core import serializers

def index(request):
    return HttpResponse("Hello Watchlist")


def html(request):
    return HttpResponse("Hello html")


def json(request):
    return HttpResponse(serializers.serialize("json", MyWatchList.objects.all()), content_type="application/json")


def xml(request):
    return HttpResponse(serializers.serialize("xml", MyWatchList.objects.all()), content_type="application/xml")