from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Task(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    FIELD = 'FI'
    OPERATION_CENTER = 'OC'
    BOTH = 'BO'
    PLACE_CHOICES = (
        (FIELD, _('field')),
        (OPERATION_CENTER, _('operation_center')),
        (BOTH, _('both')),
    )
    place = models.CharField(
        max_length=2,
        choices=PLACE_CHOICES,
        default=FIELD,
    )

    time_beginning = models.TimeField()
    time_ending = models.TimeField()
    min_volunteers = models.IntegerField()
    max_volunteers = models.IntegerField()


class Volunteer(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )

    car_availability = models.BooleanField(verbose_name=_("Car availability"),
                                           help_text=_("car_availability_help_text"), default=False)

    def __str__(self):
        volunteer_str = self.user.get_full_name()
        if volunteer_str is not '':
            return volunteer_str
        else:
            return self.user.get_username()
