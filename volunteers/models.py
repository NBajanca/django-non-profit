from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _


class Volunteer(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),

        on_delete=models.CASCADE,
    )

    car_availability = models.BooleanField(verbose_name=_("Car availability"), help_text=_("car_availability_help_text")
                                           , default=False)

    def __str__(self):
        volunteer_str = self.user.get_full_name()
        if volunteer_str is not '':
            return volunteer_str
        else:
            return self.user.get_username()


class VolunteerComplementaryContact(models.Model):
    volunteer = models.ForeignKey(
        Volunteer,
        related_name = 'volunteer_complementary_contact_list',
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

    def __str__(self):
        return str(self.volunteer) + ' - ' + self.first_name + ' ' +self.last_name
