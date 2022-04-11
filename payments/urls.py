from django.urls import path, include
from . import views

urlpatterns = [
    path('stripe/', include('djstripe.urls', namespace='djstripe')),
    path('checkout/', views.checkout, name='checkout'),
    path("create-subscription/", views.create_subscription, name="create_sub"),
    path("complete/", views.complete, name="complete"),
    path("cancel/", views.cancel, name="cancel"),
]
