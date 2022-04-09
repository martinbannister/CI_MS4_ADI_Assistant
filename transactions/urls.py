from django.urls import path

from .views import (
    AccountingCodeListView,
    AccoutingCodeDetailView,
    AccoutingCodeEditView,
    AccoutingCodeDeleteView,
    AccountingCodeCreateView,
    TransactionListView,
    TransactionDetailView,
    TransactionEditView,
    TransactionDeleteView,
    TransactionCreateView,
    )

urlpatterns = [
    # Accounting Codes
    path(
        'codes/<int:pk>/',
        AccoutingCodeDetailView.as_view(),
        name='acc_code_detail'
        ),
    path(
        'codes/<int:pk>/edit/',
        AccoutingCodeEditView.as_view(),
        name='acc_code_edit'
    ),
    path(
        'codes/<int:pk>/delete/',
        AccoutingCodeDeleteView.as_view(),
        name='acc_code_delete'
    ),
    path(
        'codes/new/',
        AccountingCodeCreateView.as_view(),
        name='acc_code_create'
    ),
    path(
        "codes/",
        AccountingCodeListView.as_view(),
        name='acc_code_list'
        ),
    # Transactions
    path(
        '<int:pk>/',
        TransactionDetailView.as_view(),
        name='trans_detail'
        ),
    path(
        '<int:pk>/edit/',
        TransactionEditView.as_view(),
        name='trans_edit'
    ),
    path(
        '<int:pk>/delete/',
        TransactionDeleteView.as_view(),
        name='trans_delete'
    ),
    path(
        'new/',
        TransactionCreateView.as_view(),
        name='trans_create'
    ),
    path(
        '',
        TransactionListView.as_view(),
        name='trans_list'
        ),
]
