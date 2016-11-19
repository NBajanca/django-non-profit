from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()


class CaptchaPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, max_length=254)
    captcha = ReCaptchaField()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),}
