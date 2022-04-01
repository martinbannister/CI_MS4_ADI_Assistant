from django.contrib import admin
from .models import Transaction, AccountingCode


class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('transaction_uuid', 'amount')

    fields = (
        'transaction_uuid',
        'owner',
        'transaction_date',
        'accounting_code',
        'customer',
        'description',
        'rate',
        'hours',
        'amount_in',
        'amount_out',
        'amount',
    )

    list_display = (
        'transaction_uuid',
        'owner',
        'description',
        'amount',
    )

    ordering = ('transaction_date',)


class AccountingCodeAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'code',
        'description',
    )

    ordering = ('owner', 'code',)


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(AccountingCode)
