from axes.utils import reset as axes_reset
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import Http404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from ipware.ip import get_ip  # Dev

from main.forms import CaptchaForm, UserForm
from volunteers.forms import VolunteerForm


@login_required
def index(request):
    return render(request, 'main/index.html')


class ProfileView(DetailView):
    model = User
    template_name = 'main/profile.html'


def edit_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404

    context = dict()
    context['user_object'] = user
    context['form_user'] = UserForm(instance=user)
    if user.volunteer is not None:
        context['form_volunteer'] = VolunteerForm(instance=user.volunteer)

    return render(request, 'main/edit_profile.html', context)


def edit_profile_user(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            updated_user = User.objects.get(pk=pk)

            response_code = 200
            response_data = model_to_dict(updated_user, fields=['username', 'first_name', 'last_name'])

        else:
            response_code = 400
            response_data = form.errors

        return JsonResponse(
            response_data,
            status=response_code,
        )

    else:
        raise Http404


def locked_out(request):
    form = CaptchaForm
    no_ip = False

    if request.method == 'POST':
        form = form(data=request.POST)
        if form.is_valid():
            # ip = get_real_ip(request)  # Prod
            ip = get_ip(request)  # Dev
            if ip is not None:
                axes_reset(ip=ip)
                return HttpResponseRedirect(reverse_lazy('main:login'))
            else:
                no_ip = True

    return render(request, 'main/locked_out.html', {'form': form, 'no_ip': no_ip})