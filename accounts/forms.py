from django import forms


class UserLoginForm(forms.form):
    """The form used to log in users"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

