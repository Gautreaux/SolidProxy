from re import L
from django.db import models

# Create your models here.

class SWModel(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.title