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
    business_name = models.CharField(
        "What is the name of your business?", max_length=50)
    website = models.CharField(
        "What kind of website would you like?", max_length=50, choices=WEBSITE_CHOICES)
    functionality = models.CharField(
        "What would you like users to do on your website?", max_length=1000)
    url = models.CharField(
        "If you already have a website please add the URL here", max_length=200, null=True, blank=True)
    business_type = models.CharField(
        "What does your business do?", max_length=2000)
    customer = models.CharField(
        "Who are your main customers/clients?", max_length=2000)
    message = models.CharField(
        "Please provide any extra information that you think might be useful", max_length=3000)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    pay_deposit = models.BooleanField(default=False)
    deposit_paid = models.BooleanField(default=False)
    pay_final = models.BooleanField(default=False)
    final_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.business_name


class question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    question = models.CharField(max_length=3000)
    Answer = models.CharField(max_length=3000)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
