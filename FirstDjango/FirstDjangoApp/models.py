from django.db import models

# Create your models here.

class Burgers(models.Model):
    title = models.CharField(max_length=200)
    size = models.CharField(max_length=200)