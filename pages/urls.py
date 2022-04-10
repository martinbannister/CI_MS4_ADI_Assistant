from django.urls import path

from .views import DashboardView, IndexView, SettingsView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('', IndexView.as_view(), name='home'),
]
