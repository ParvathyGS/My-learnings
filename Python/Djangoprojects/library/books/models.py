from django.db import models

# Create your models here.
class Book_details(models.Model):
	book_name = models.CharField(max_length=100)
	author_name = models.CharField(max_length=100)
	year = models.IntegerField()
	