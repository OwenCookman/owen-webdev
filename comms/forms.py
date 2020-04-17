from django import forms


class ContactForm(forms.Form):
    """The form users use to give information on the website
    they would like to have built"""
    message = forms.CharField(
        widget=forms.Textarea, label="Please enter a message here, give as much information as possible that you think may be useful")
