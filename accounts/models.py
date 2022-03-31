from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):

    class AccountType(models.IntegerChoices):
        PDI = 0, _('PDI')
        ADI = 1, _('ADI')
        PUPIL = 2, _('Pupil')

    account_type = models.IntegerField(choices=AccountType.choices)
