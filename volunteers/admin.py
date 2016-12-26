from django.contrib import admin
from .models import Volunteer, Shift, Task, Preference, VolunteerShift, VolunteerUnavailability, VolunteerPresence


class ShiftInline(admin.TabularInline):
    extra = 5
    model = Shift


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = (ShiftInline,)
    prepopulated_fields = {"slug": ("name",)}


class PreferenceInline(admin.TabularInline):
    extra = 3
    model = Preference


class VolunteerShiftInline(admin.TabularInline):
    extra = 1
    model = VolunteerShift


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    inlines = (PreferenceInline, VolunteerShiftInline,)


admin.site.register(Shift)
admin.site.register(Preference)
admin.site.register(VolunteerShift)
admin.site.register(VolunteerUnavailability)
admin.site.register(VolunteerPresence)
