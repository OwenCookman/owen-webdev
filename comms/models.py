from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class query(models.Model):
    website = models.CharField(max_length=200)
    functionality = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    business = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
