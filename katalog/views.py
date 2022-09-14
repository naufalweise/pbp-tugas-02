from django.shortcuts import render
from .models import CatalogItem

STUDENT_NAME = "NAUFAL WEISE WIDYATAMA"
STUDENT_ID = "2106750263"

def index(request):
    catalog_items = CatalogItem.objects.all()
    context = {'catalog_items': catalog_items, 'student_name': STUDENT_NAME, 'student_id': STUDENT_ID}
    return render(request, 'katalog.html', context)
