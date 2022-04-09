from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Transaction, AccountingCode


class TestTransactionViews(TestCase):
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

        cls.trans = Transaction.objects.create(
            owner=cls.user,
            transaction_date=timezone.now(),
            accounting_code=cls.accCode,
            description='test transaction',
            amount_in=1
        )

    def test_get_transaction_list(self):
        response = self.client.get('/transactions/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trans_list.html')

    def test_get_trans_detail_page(self):
        response = self.client.get(
            reverse('trans_detail', kwargs={'pk': self.trans.pk})
        )
        no_response = self.client.get('/transactions/999999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test transaction')
        self.assertTemplateUsed(response, 'trans_detail.html')

    def test_get_edit_trans_page(self):
        response = self.client.get(
            reverse('trans_edit', kwargs={'pk': self.trans.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trans_edit.html')

    def test_get_delete_trans_page(self):
        response = self.client.get(
            reverse('trans_delete', kwargs={'pk': self.trans.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trans_delete.html')

    def test_get_create_trans_page(self):
        response = self.client.get('/transactions/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trans_create.html')

    def test_edit_trans(self):
        pass

    def test_delete_trans(self):
        pass


class TestAccoutingCodeViews(TestCase):
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

    def test_get_code_list(self):
        response = self.client.get('/transactions/codes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounting_code_list.html')

    def test_get_code_detail(self):
        response = self.client.get(
            reverse('acc_code_detail', kwargs={'pk': self.accCode.pk})
        )
        no_response = self.client.get('/transactions/codes/999999/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test accounting code')
        self.assertTemplateUsed(response, 'accouting_code_detail.html')

    def test_edit_code_page(self):
        response = self.client.get(
            reverse('acc_code_edit', kwargs={'pk': self.accCode.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accouting_code_edit.html')

    def test_delete_code_page(self):
        pass

    def test_code_create_view(sefl):
        pass
