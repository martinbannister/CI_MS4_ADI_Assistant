from django.urls import path

from .views import (
    AccountingCodeListView,
    AccoutingCodeDetailView,
    AccoutingCodeEditView,
    AccoutingCodeDeleteView,
    AccountingCodeCreateView,
    )

urlpatterns = [
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
]
