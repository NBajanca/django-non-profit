from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm


class CaptchaForm(forms.Form):
    captcha = ReCaptchaField()


class CaptchaPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, max_length=254)
    captcha = ReCaptchaField()