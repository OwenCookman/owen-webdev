from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class query(models.Model):
    website = models.CharField(
        max_length=200, label="What kind of website are you looking for?*")
    functionality = models.CharField(
        max_length=200, label="What functionality would you like on your website?*")
    url = models.CharField(
        max_length=200, label="pre existing websites URL", required="False")
    designs = models.FileInput()
    business = models.CharField(max_length=200,
                                widget=Textarea, label="What does your business do?")
    customer = models.CharField(max_length=200,
                                widget=Textarea, label="Who are your clients/customers?")
    message = models.CharField(max_length=200,
                               widget=Textarea, label="Please enter a message here, give as much information as possible that you think may be useful")

    user = models.ForeignKey(User)
