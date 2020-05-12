from django import forms
from . import models


class ContactForm(forms.ModelForm):
    """ Form used to create new orders """
    class Meta:
        model = models.order
        fields = [
            'business_name', 'website',
            'functionality', 'url',
            'business_type', 'customer',
            'message',
        ]
        widgets = {
            'website': forms.RadioSelect(),
            'functionality': forms.Textarea(),
            'business_type': forms.Textarea(),
            'customer': forms.Textarea(),
            'message': forms.Textarea(),
        }


class QuestionForm(forms.ModelForm):
    """ Form used by none registered users to create new questions """
    class Meta:
        model = models.question
        fields = [
            'name', 'email',
            'question',
        ]
        widgets = {
            'question': forms.Textarea(),
        }


class UserQuestionForm(forms.ModelForm):
    """ Form used by registered users to create new questions """
    class Meta:
        model = models.question
        fields = [
            'question',
        ]
        widgets = {
            'question': forms.Textarea()
        }
