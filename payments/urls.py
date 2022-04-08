from django.urls import path, include
from .views import checkout

urlpatterns = [
    path('stripe/', include('djstripe.urls', namespace='djstripe')),
    path('checkout/', checkout, name='checkout'),
]
