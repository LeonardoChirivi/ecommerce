from django import forms
from django.contrib.auth.models import User


class ProductAddToCartForm(forms.Form):
    pass


class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            # 'First Name',
            # 'Last Name',
            # 'E-mail',
            'username',
            'password',
        ]
