from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import ugettext as _

from main.models import ExtendedUser


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
                   'last_name': forms.TextInput(attrs={'class': 'form-control'})}


class ExtendedUserForm(ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ['date_of_birth', 'mobile_phone', 'address', 'academic_qualifications',
                  'profession', 'volunteer_experience', 'observations']
        widgets = {'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
                   'mobile_phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'academic_qualifications': forms.TextInput(attrs={'class': 'form-control'}),
                   'profession': forms.TextInput(attrs={'class': 'form-control'}),
                   'volunteer_experience': forms.Textarea(attrs={'class': 'form-control'}),
                   'observations': forms.Textarea(attrs={'class': 'form-control'})}


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class EmailChangeForm(forms.Form):
    """
    A form that lets a user change set their email while checking for change in the e-mail.
    """
    error_messages = {
        'email_mismatch': _("The two email addresses fields didn't match."),
        'not_changed': _("The email address is the same as the one already defined."),
    }

    new_email1 = forms.EmailField(
        label=_("New email address"),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    new_email2 = forms.EmailField(
        label=_("New email address confirmation"),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError(
                    self.error_messages['not_changed'],
                    code='not_changed',
                )
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError(
                    self.error_messages['email_mismatch'],
                    code='email_mismatch',
                )
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user
