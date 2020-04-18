from django import forms
from .models import query


class ContactForm(forms.ModelForm):
    class Meta:
        model = query
        fields = (website, functionality, url, business, customer, message)
    