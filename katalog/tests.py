from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CatalogItem

class CatalogItemTestCase(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Item 1", item_price=10000, item_stock=10, description="Desc 1", rating=8, item_url="https://example.com/item1")
        CatalogItem.objects.create(item_name="Item 2", item_price=10000, item_stock=10, description="Desc 1", rating=7, item_url="https://example.com/item2")
        CatalogItem.objects.create(item_name="Item 3", item_price=10000, item_stock=10, description="Desc 1", rating=1, item_url="https://example.com/item3")

    def test_katalog_count(self):
        """CatalogItem yang berada di database memiliki jumlah yang sesuai"""
        catalog_list = CatalogItem.objects.all()
        self.assertTrue(len(catalog_list), 3)

    def test_rating_validation(self):
        """Tiap item harus memiliki rating dalam range 0 sampai 10, inklusif."""
        catalog_list = CatalogItem.objects.all()
        for item in catalog_list:
            self.assertTrue(0 <= item.rating <= 10)