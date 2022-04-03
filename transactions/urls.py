from django.urls import path

from .views import AccountingCodeListView

urlpatterns = [
    path("accountscodes/", AccountingCodeListView.as_view(), name='acc_code_list')
]
