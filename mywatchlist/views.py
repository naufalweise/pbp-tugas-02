from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Watchlist")

def html(request):
    return HttpResponse("Hello html")
def json(request):
    return HttpResponse("Hello json")
def xml(request):
    return HttpResponse("Hello xml")