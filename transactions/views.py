from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Transaction, AccountingCode
from .forms import TransactionForm


class AccountingCodeListView(ListView):
    model = AccountingCode
    template_name = 'accounting_code_list.html'


class AccoutingCodeDetailView(DetailView):
    model = AccountingCode
    template_name = 'accouting_code_detail.html'


class AccoutingCodeEditView(UpdateView):
    model = AccountingCode
    fields = (
        'code',
        'description',
    )
    template_name = 'accouting_code_edit.html'


class AccoutingCodeDeleteView(DeleteView):
    model = AccountingCode
    template_name = 'accouting_code_delete.html'
    success_url = reverse_lazy('accounting_code_list.html')


class AccountingCodeCreateView(CreateView):
    model = AccountingCode
    template_name = 'accounting_code_create.html'
    fields = (
        'code',
        'description',
    )

    # REF: https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Transactions


class TransactionListView(ListView):
    model = Transaction
    template_name = 'trans_list.html'


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'trans_detail.html'


class TransactionEditView(UpdateView):
    model = Transaction
    template_name = 'trans_edit.html'
    form_class = TransactionForm


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'trans_delete.html'
    success_url = reverse_lazy('trans_list.html')


class TransactionCreateView(CreateView):
    model = Transaction
    template_name = 'trans_create.html'
    form_class = TransactionForm

    # REF: https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
