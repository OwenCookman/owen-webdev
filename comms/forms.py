from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.order
        fields = [
            'business_name', 'website',
            'functionality', 'url',
            'business_type', 'customer',
            'message'
        ]
        widgets = {
            'website': forms.RadioSelect(),
            'functionality': forms.CheckboxSelectMultiple(),
            'business_type': forms.Textarea(),
            'customer': forms.Textarea(),
            'message': forms.Textarea(),
        }
