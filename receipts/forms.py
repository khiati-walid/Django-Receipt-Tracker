from django import forms
from .models import Receipt


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["store_name", "date_of_purchase", "item_list", "total_amount"]
