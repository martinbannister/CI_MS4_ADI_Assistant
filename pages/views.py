from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


class IndexView(TemplateView):
    template_name = 'index.html'
