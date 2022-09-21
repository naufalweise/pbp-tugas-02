from django.urls import path
from mywatchlist.views import index
from . import views

app_name = 'mywatchlist'

urlpatterns = [
    path('', index, name='index'),
    path('json/', views.json, name='json'),
    path('xml/', views.xml, name='xml'),
    path('xml/<int:id>', views.xml_by_id, name='xml_by_id'),
    path('json/<int:id>', views.json_by_id, name='json_by_id'),
    path('html/', views.html, name='html'),
]