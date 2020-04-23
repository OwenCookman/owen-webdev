from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class order(models.Model):
    WEBSITE_CHOICES = (
        ('Landing page/Brochure website', 'Landing page/Brochure website'),
        ('Multipaged information website',
         'Multipaged information website'),
        ('Ecommerce/Webstore', 'Ecommerce/Webstore'),
        ('Something Else', 'Something Else')
    )
    # FUNCTIONALITY_CHOICES = (
    #     ('Online Payments', 'Online Payments'),
    #     ('Shopping Cart/Checkout', 'Shopping Cart/Checkout'),
    #     ('User Registration & Login', 'User Registration & Login'),
    #     ('Something Else', 'Something Else')
    # )
    business_name = models.CharField(
        "What is the name of your business?", max_length=50)
    website = models.CharField(
        "What kind of website would you like?", max_length=50, choices=WEBSITE_CHOICES)
    functionality = models.CharField(
        "What would you like users to do on your website?", max_length=200)
    url = models.CharField(
        "If you already have a website please add the URL here", max_length=200)
    business_type = models.CharField(
        "What does your business do?", max_length=200)
    customer = models.CharField(
        "Who are your main customers/clients?", max_length=200)
    message = models.CharField(
        "Please provide any extra information that you think might be useful", max_length=200)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
