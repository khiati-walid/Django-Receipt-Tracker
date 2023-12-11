from django.urls import path
from .views import (
    receipt_list,
    receipt_detail,
    receipt_new,
    receipt_edit,
    receipt_delete,
)

urlpatterns = [
    path("", receipt_list, name="receipt_list"),
    path("receipt/<int:pk>/", receipt_detail, name="receipt_detail"),
    path("receipt/new/", receipt_new, name="receipt_new"),
    path("receipt/<int:pk>/edit/", receipt_edit, name="receipt_edit"),
    path("receipt/<int:pk>/delete/", receipt_delete, name="receipt_delete"),
]
