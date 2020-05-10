from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class invoice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)
    business_name = models.CharField(max_length=50)
    start_date = models.DateField()
    invoice_date = models.DateField(auto_now_add=True)
    card_type = models.CharField(max_length=20)
    last4 = models.CharField(max_length=4)
    amount_charged = models.FloatField()
    remaining_cost = models.FloatField()
    stripe_receipt = models.CharField(max_length=1000)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.business_name
