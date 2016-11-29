from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
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


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control'
        })

