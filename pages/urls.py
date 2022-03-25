from django.urls import path

from .views import DashboardView, IndexView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', IndexView.as_view(), name='home'),
]
