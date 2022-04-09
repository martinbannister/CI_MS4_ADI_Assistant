from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Transaction, AccountingCode


class TestTransactionCreate(TestCase):
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

    def test_create_trans_postive_amount(self):
        response = self.client.post(
            reverse('trans_create'),
            data={
                'owner': self.user.id,
                'transaction_date': timezone.now(),
                'accounting_code': self.accCode.id,
                'description': 'test create positive transaction',
                'amount_in': 1,
            },
        )
        self.assertEqual(response.status_code, 200)
        new_trans = Transaction.objects.first()
        self.assertEqual(
            new_trans.description,
            'test create positive transaction'
        )
        self.assertEqual(new_trans.amount, 1)

    def test_create_trans_no_amount(self):
        response = self.client.post(
            reverse('trans_create'),
            {
                'owner': self.user.id,
                'transaction_date': timezone.now(),
                'accounting_code': self.accCode.id,
                'description': 'test transaction without amount in or out',
            },
        )
        # REF: https://stackoverflow.com/questions/10991239/django-test-non-field-validation-errors/#34084632
        self.assertFormError(
            response,
            'form',
            None,
            'Either Amount In or Out are required'
        )

    def test_create_trans_negative_amount(self):
        response = self.client.post(
            reverse('trans_create'),
            {
                'owner': self.user.id,
                'transaction_date': timezone.now(),
                'accounting_code': self.accCode.id,
                'description': 'test create negative transaction',
                'amount_out': -1
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Transaction.objects.last().description,
            'test create negative transaction'
        )
        self.assertEqual(
            Transaction.objects.last().amount,
            -1
        )
