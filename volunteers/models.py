from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _


class Volunteer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    date_of_birth = models.DateField(verbose_name=_("Date of birth"), null=True, blank=True)
    mobile_phone = PhoneNumberField(verbose_name=_("Mobile phone number"))
    car_availability = models.BooleanField(verbose_name=_("Car availability"), help_text=_("car_availability_help_text")
                                           , default=False)
    address = models.CharField(max_length=120, verbose_name=_("Adress"), help_text=_("address_help_text"), blank=True)
    academic_qualifications = models.CharField(max_length=80, verbose_name=_("Academic qualifications"), blank=True)
    profession = models.CharField(max_length=80, verbose_name=_("Profession"), blank=True)
    volunteer_experience = models.TextField(verbose_name=_("Volunteer Experience"), blank=True)
    observations = models.TextField(verbose_name=_("Observations"), blank=True)


class VolunteerComplementaryContact(models.Model):
    volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(max_length=30, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("First Name"))

    ICE = 'ICE'
    GUARDIAN = 'GAR'
    REFERRAL = 'REF'
    CONTACT_TYPE = (
        (ICE, _("Contact in Case of Emergency")),
        (GUARDIAN, _("Guardian")),
        (REFERRAL, _("Referral")),
    )
    contact_type = models.CharField(
        max_length=3,
        choices=CONTACT_TYPE,
        default=ICE,
    )

    mobile_phone = PhoneNumberField(verbose_name=_("Mobile phone number"), blank=True)
    email = models.EmailField(verbose_name=_("Email"), blank=True)
    relation = models.CharField(max_length=80, verbose_name=_("Relation"), blank=True)