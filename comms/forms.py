from django import forms


class ContactForm(forms.form):
    """The form users use to give information on the website
    they would like to have built"""
    Question1 = forms.BooleanField(
        label="A Brochure/landing page", required=True)
