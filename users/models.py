from django.db import models
from books.models import Item
 # Create your models here.

class Users(models.Model):
    userId=models.IntegerField()
    favourites = models.ManyToManyField(Item,related_name="liked_by")