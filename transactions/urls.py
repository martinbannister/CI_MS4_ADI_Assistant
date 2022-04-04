from django.urls import path

from .views import (
    AccountingCodeListView,
    AccoutingCodeDetailView,
    AccoutingCodeEditView,
    AccoutingCodeDeleteView
    )

urlpatterns = [
    path(
        '<int:pk>/',
        AccoutingCodeDetailView.as_view(),
        name='acc_code_detail'
        ),
    path(
        '<int:pk>/edit/',
        AccoutingCodeEditView.as_view(),
        name='acc_code_edit'
    ),
    path(
        '<int:pk>/delete',
        AccoutingCodeDeleteView.as_view(),
        name='acc_code_delete'
    ),
    path(
        "accountscodes/",
        AccountingCodeListView.as_view(),
        name='acc_code_list'
        ),
]
