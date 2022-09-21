from django.test import TestCase, Client
from .models import MyWatchList
import datetime

class MyWatchListTestCase(TestCase):
    def setUp(self):
        MyWatchList.objects.create(title="Movie 1", rating=3, release_date=datetime.date.today(), review = "Review 1")
        MyWatchList.objects.create(title="Movie 2", rating=3, release_date=datetime.date.today(), review = "Review 2")

    def test_endpoints(self):
        """Test tiap endpoint urls memiliki status code 200"""
        client = Client()

        response = client.get("/mywatchlist/json/")
        self.assertEqual(response.status_code, 200)
        response = client.get("/mywatchlist/xml/")
        self.assertEqual(response.status_code, 200)
        response = client.get("/mywatchlist/html/")
        self.assertEqual(response.status_code, 200)