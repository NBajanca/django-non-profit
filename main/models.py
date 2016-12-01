from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _


class ExtendedUser(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,

    )

    date_of_birth = models.DateField(verbose_name=_("Date of birth"), help_text=_("date_of_birth_help_text"), null=True, blank=True)
    mobile_phone = PhoneNumberField(verbose_name=_("Mobile phone number"), help_text=_("mobile_phone_help_text"))
    address = models.CharField(max_length=120, verbose_name=_("Address"), help_text=_("address_help_text"), blank=True)
    academic_qualifications = models.CharField(max_length=80, verbose_name=_("Academic qualifications"), blank=True)
    profession = models.CharField(max_length=80, verbose_name=_("Profession"), blank=True)
    volunteer_experience = models.TextField(verbose_name=_("Volunteer Experience"), blank=True)
    observations = models.TextField(verbose_name=_("Observations"), blank=True)

    def __str__(self):
        user_full_name = self.user.get_full_name()
        if user_full_name is not '':
            return user_full_name
        else:
            return self.user.get_username()
