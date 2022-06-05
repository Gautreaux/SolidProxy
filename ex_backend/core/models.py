from re import L
from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title

class SWModel(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.title