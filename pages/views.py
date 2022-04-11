import stripe
from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import UserProfile


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


def index_view(request):
    """ Display current user options
        or welcome page
    """
    if request.user:
        context = {
            'user': request.user,
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'settings.html'
