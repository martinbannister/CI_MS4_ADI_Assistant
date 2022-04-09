from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from .models import AccountingCode
from .forms import TransactionForm


class TestTransactionCreateForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='notasecret',
            account_type=0
        )

        cls.accCode = AccountingCode.objects.create(
            owner=cls.user,
            code=9999,
            description='test accounting code'
        )

    def test_amount_in_or_out_is_required(self):
        form = TransactionForm(
            {
                'owner': self.user.id,
                'transaction_date': timezone.now(),
                'accounting_code': self.accCode.id,
                'description': 'test transaction without amount in or out'
            }
        )
        self.assertFalse(form.is_valid())
