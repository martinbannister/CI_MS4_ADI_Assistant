from decimal import Decimal
from django.core import validators
from django.utils.translation import gettext_lazy as _
import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse


class Transaction(models.Model):
    transaction_uuid = models.CharField(
                                        max_length=32,
                                        null=False,
                                        editable=False
                                       )
    owner = models.ForeignKey(
                              settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE
                             )
    transaction_date = models.DateField(
                                        _("Transaction Date"),
                                        null=False,
                                        blank=False
                                       )
    accounting_code = models.ForeignKey("AccountingCode",
                                        on_delete=models.CASCADE)
    customer = models.ForeignKey("customers.customer",
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    rate = models.DecimalField(max_digits=5, decimal_places=2,
                               null=True, blank=True)
    hours = models.DecimalField(max_digits=3, decimal_places=1,
                                null=True, blank=True)
    # REF: https://stackoverflow.com/questions/61350975/how-can-i-have-only-positive-decimal-numbers-in-django-using-python
    amount_in = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validators.MinValueValidator(Decimal('0.01'))],
        null=True,
        blank=True
        )
    amount_out = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validators.MaxValueValidator(Decimal('0'))],
        null=True,
        blank=True
        )
    amount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        editable=False
        )

    def _generate_trans_number(self):
        """
        Generate a random, unique transaction number
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Overwrite default save method to
        add a unique transaction number
        and update the amount field
        """
        if not self.transaction_uuid:
            self.transaction_uuid = self._generate_trans_number()

        if self.amount_in:
            self.amount = self.amount_in
        else:
            self.amount = self.amount_out

        super().save(*args, **kwargs)

    def __str__(self):
        return self.transaction_uuid

    def get_absolute_url(self):
        return reverse("trans_detail", kwargs={"pk": self.pk})


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

    def __str__(self):
        return f'{self.code} - {self.description}'
    
    def get_absolute_url(self):
        return reverse("acc_code_detail", kwargs={"pk": self.pk})
    
