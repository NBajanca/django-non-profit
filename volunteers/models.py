from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
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
    min_volunteers = models.PositiveSmallIntegerField()
    max_volunteers = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Shift(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    MONDAY = '1'
    TUESDAY = '2'
    WEDNESDAY = '3'
    THURSDAY = '4'
    FRIDAY = '5'
    SATURDAY = '6'
    SUNDAY = '7'
    DAY_OF_THE_WEEK = (
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    )
    day_of_the_week = models.CharField(
        max_length=2,
        choices=DAY_OF_THE_WEEK
    )

    class Meta:
        unique_together = ('task', 'day_of_the_week',)

    def __str__(self):
        return self.task.name + ' (' + self.get_day_of_the_week_display() + ')'


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


class Preference(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    priority = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ])

    class Meta:
        unique_together = ('volunteer', 'shift',)

    def __str__(self):
        return '[' + str(self.priority) + '] ' + str(self.volunteer) + ' - ' + str(self.shift)


class VolunteerShift(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    WEEKLY = 'W'
    BIWEEKLY = 'B'
    MONTHLY = 'M'
    FREQUENCY = (
        (WEEKLY, _('Weekly')),
        (BIWEEKLY, _('Biweekly')),
        (MONTHLY, _('Monthly')),
    )
    frequency = models.CharField(
        max_length=1,
        choices=FREQUENCY,
        default=WEEKLY,
    )

    class Meta:
        unique_together = ('volunteer', 'shift',)

    def __str__(self):
        return  str(self.volunteer) + ' - ' + str(self.shift)


class VolunteerUnavailability(models.Model):
    volunteer_shift = models.ForeignKey(VolunteerShift, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + ' - ' + str(self.volunteer_shift)


class VolunteerPresence(models.Model):
    volunteer_shift = models.ForeignKey(VolunteerShift, on_delete=models.CASCADE)
    date = models.DateField()
    presence = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + ' - ' + str(self.volunteer_shift)


