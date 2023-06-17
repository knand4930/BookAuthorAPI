from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    publication_year = models.DateField(blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
