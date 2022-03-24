from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):

    class Subscription(models.IntegerChoices):
        FREE = 0, _('Complimentary')
        PDI = 1, _('Trainee (6 month)')
        ADI = 2, _('Driving Instuctor (monthly)')
        ADI_A = 3, _('Driving Instuctor (annual)')

        __empty__ = ('Choose a subscription')

    subscription = models.IntegerField(choices=Subscription.choices, default=0)
    sub_duration = models.IntegerField(null=False, blank=False, default=0)
    sub_start_date = models.DateTimeField(null=False, blank=False,
                                          default=timezone.now)
    sub_end_date = models.DateTimeField(null=False, blank=False,
                                        default=timezone.now)

    address1 = models.CharField(max_length=80, null=False, blank=False,
                                default='7 Sundorne')
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False,
                            default='Wrecsam')
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=False,
                                default='LL13 0EB')
    country = models.CharField(max_length=40, null=False, blank=False,
                               default='UK')
