from django import forms
from .models import Receipt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ["store_name", "date_of_purchase", "item_list", "total_amount"]
        widgets = {
            "date_of_purchase": forms.DateInput(attrs={"type": "date"}),
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name in ["username", "password1", "password2"]:
            self.fields[field_name].help_text = None
