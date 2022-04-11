from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:pk>/',
        views.CustomerDetailView.as_view(),
        name='customer_detail'
        ),
    path(
        '<int:pk>/edit/',
        views.CustomerEditView.as_view(),
        name='customer_edit'
    ),
    path(
        '<int:pk>/delete/',
        views.CustomerDeleteView.as_view(),
        name='customer_delete'
    ),
    path(
        'new/',
        views.CustomerCreateView.as_view(),
        name='customer_create'
    ),
    path(
        "",
        views.CustomerListView.as_view(),
        name='customer_list'
        ),
]
