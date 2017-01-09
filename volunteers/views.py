from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from volunteers.models import Volunteer


@login_required
def index(request):
    context = dict()
    context['num_volunteers'] = Volunteer.objects.all().count()
    context['num_volunteers_inactive'] = Volunteer.objects.filter(user__is_active=False).count()
    context['num_volunteers_working'] = Volunteer.objects.filter(user__is_active=True, volunteershift__isnull=False).\
        distinct().count()
    context['num_volunteers_active_not_working'] = (context['num_volunteers'] - (context['num_volunteers_inactive'] +
                                                    context['num_volunteers_working']))

    return render(request, 'volunteers/index.html', context)
