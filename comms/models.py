from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class order(models.Model):
    WEBSITE_CHOICES = (
        ('Landing page/Brochure website', 'Landing page/Brochure website'),
        ('Multipaged information website',
         'Multipaged information website'),
        ('Ecommerce/Webstore', 'Ecommerce/Webstore'),
        ('Something Else', 'Something Else')
    )
    FUNCTIONALITY_CHOICES = (
        ('Online Payments', 'Online Payments'),
        ('Shopping Cart/Checkout', 'Shopping Cart/Checkout'),
        ('User Registration & Login', 'User Registration & Login'),
        ('Something Else', 'Something Else')
    )
    website = models.CharField(max_length=50, choices=WEBSITE_CHOICES)
    functionality = models.CharField(
        max_length=50, choices=FUNCTIONALITY_CHOICES)
    url = models.CharField(max_length=200)
    business = models.CharField(max_length=200)
    customer = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
