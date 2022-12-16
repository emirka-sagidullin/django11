from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Autors(models.Model):
    name = models.CharField(max_length=50)

class Publisher(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    heading = models.CharField(max_length=20)
    url = models.URLField()
    content = models.TextField()
    publication = models.CharField(max_length=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autors, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
