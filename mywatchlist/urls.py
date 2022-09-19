from django.urls import path
from mywatchlist.views import index

app_name = 'mywatchlist'

urlpatterns = [
    path('', index, name='index'),
]