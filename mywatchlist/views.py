from django.http import HttpResponse
from .models import MyWatchList
from django.core import serializers
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello Watchlist")


def html(request):
    data = MyWatchList.objects.all()
    return render(request, "mywatchlist.html", {"mywatchlist": data})


def json(request):
    return HttpResponse(serializers.serialize("json", MyWatchList.objects.all()), content_type="application/json")


def xml(request):
    return HttpResponse(serializers.serialize("xml", MyWatchList.objects.all()), content_type="application/xml")