from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)