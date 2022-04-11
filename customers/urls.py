from django.urls import path
from . import views

urlpatterns = [
    path('import/', views.import_contacts, name='import_contacts')
]
