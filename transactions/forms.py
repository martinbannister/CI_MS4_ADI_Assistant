from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'transaction_date',
            'accounting_code',
            'customer',
            'description',
            'rate',
            'hours',
            'amount_in',
            'amount_out',
        )

    def __init__(self, *args, **kwargs):
        """

        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'transaction_date': 'Date',
            'accounting_code': 'Accouting Code',
            'customer': 'Customer',
            'description': 'Description',
            'rate': 'Hourly Rate',
            'hours': 'Number of Hours',
            'amount_in': 'Amount In',
            'amount_out': 'Amount Out',
        }

        self.fields['transaction_date'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe_style_input'
            self.fields[field].label = False

    def clean(self):
        # REF: https://stackoverflow.com/questions/50643395/make-one-field-as-mandatory-in-two-fields-in-django-forms
        # REF: https://docs.djangoproject.com/en/dev/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other
        cleaned_data = super().clean()
        amount_in = cleaned_data.get('amount_in')
        amount_out = cleaned_data.get('amount_out')

        if not amount_in and not amount_out:
            raise forms.ValidationError(
                'Either Amount In or Out are required'
            )
