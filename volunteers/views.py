from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from volunteers.forms import CaptchaForm
from axes.utils import reset as axes_reset
# from ipware.ip import get_real_ip  # Prod
from ipware.ip import get_ip  # Dev


@login_required
def index(request):
    return render(request, 'main/index.html')


def locked_out(request):
    form = CaptchaForm
    no_ip = False

    if request.POST:
        form = form(data=request.POST)
        if form.is_valid():
            # ip = get_real_ip(request)  # Prod
            ip = get_ip(request)  # Dev
            if ip is not None:
                axes_reset(ip=ip)
                return HttpResponseRedirect(reverse_lazy('volunteers:login'))
            else:
                no_ip = True

    return render(request, 'main/locked_out.html', {'form': form, 'no_ip': no_ip})