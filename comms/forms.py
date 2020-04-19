from django import forms
from .models import order


class ContactForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['website', 'functionality', 'url', 'business', 'customer', 'message']
    