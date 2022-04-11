from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Customer


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer_detail.html'


class CustomerEditView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = (
        'firstname',
        'lastname',
        'customer_type',
        'hourly_rate',
        'balance_hours',
        'balance_payment',
        'phone',
        'email',
        'address1',
        'address2',
        'town',
        'county',
        'postcode',
        'country',
        'active',
    )
    template_name = 'customer_edit.html'


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer_list.html')


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'customer_create.html'
    fields = (
        'firstname',
        'lastname',
        'customer_type',
        'hourly_rate',
        'balance_hours',
        'balance_payment',
        'phone',
        'email',
        'address1',
        'address2',
        'town',
        'county',
        'postcode',
        'country',
        'active',
    )

    # REF: https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-editing/#models-and-request-user
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
