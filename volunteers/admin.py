from django.contrib import admin
from .models import Volunteer, VolunteerComplementaryContact

# Register your models here.


class VolunteerComplementaryContactInline(admin.TabularInline):
    extra = 1
    model = VolunteerComplementaryContact


class VolunteerAdmin(admin.ModelAdmin):
    inlines = (VolunteerComplementaryContactInline,)

admin.site.register(Volunteer, VolunteerAdmin)