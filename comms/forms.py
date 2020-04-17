from django import forms


class ContactForm(forms.Form):
    """The form users use to give information on the website
    they would like to have built"""
    website = forms.CharField(label="What kind of website are you looking for?*")
    functionality = forms.CharField(label="What functionality would you like on your website?*")
    url = forms.CharField(label="pre existing websites URL", required="False")
    designs = forms.FileInput()
    business = forms.CharField(
        widget=forms.Textarea, label="What does your business do?")
    customer = forms.CharField(
        widget=forms.Textarea, label="Who are your clients/customers?")
    message = forms.CharField(
        widget=forms.Textarea, label="Please enter a message here, give as much information as possible that you think may be useful")
