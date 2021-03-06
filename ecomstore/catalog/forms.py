from django import forms
from django.contrib.auth.models import User


class ProductAddToCartForm(forms.Form):
    pass


class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        help_texts = {
            'username': None,
        }
        fields = [
            'username',
            'password',
        ]
