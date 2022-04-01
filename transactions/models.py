from decimal import Decimal
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Transaction(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    transaction_date = models.DateField(
        _("Transaction Date"),
        null=False,
        blank=False)
    accounting_code = models.ForeignKey("AccountingCode",
                                        on_delete=models.CASCADE)
    customer = models.ForeignKey("customers.customer",
                                 on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=200)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    hours = models.DecimalField(max_digits=3, decimal_places=1)
    amount_in = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validators.MinValueValidator(Decimal('0.01'))]
        )
    amount_out = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validators.MaxValueValidator(Decimal('0'))]
        )
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    balance = models.DecimalField(max_digits=8, decimal_places=2)


class AccountingCode(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    code = models.SmallIntegerField()
    description = models.CharField(max_length=100)

    # REF: https://stackoverflow.com/questions/47082753/how-to-make-field-unique-for-current-user-django
    class Meta:
        unique_together = ('owner', 'code')
