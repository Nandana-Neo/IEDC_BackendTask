from django.db import models

# Create your models here.
class Item(models.Model):
    title=models.CharField(max_length=200,default="1984")
    author=models.CharField(max_length=500,default="George Orwell")
    pages=models.IntegerField(default=328)
