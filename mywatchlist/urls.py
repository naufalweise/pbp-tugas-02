from django.urls import path
from mywatchlist.views import index
from . import views

app_name = 'mywatchlist'

urlpatterns = [
    path('', index, name='index'),
    path('json/', views.json, name='json'),
    path('xml/', views.xml, name='xml'),
]