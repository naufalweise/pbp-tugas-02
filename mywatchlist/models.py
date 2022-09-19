from platform import release
from django.db import models

class MyWatchList(models.Model):
	watched = models.BooleanField(default=False)
	title = models.CharField(max_length=255)
	rating = models.IntegerField()
	release_date = models.DateField()
	review = models.TextField()