from django import forms
from .models import order


class ContactForm(forms.ModelForm):
    class Meta:
        model = order
        exclude = ('client',)
        widgets = {
            'website': forms.RadioSelect(),
            'functionality': forms.CheckboxSelectMultiple(),
            'business_type': forms.Textarea(),
            'customer': forms.Textarea(),
            'message': forms.Textarea(),
        }
