from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["t_type", "amount", "date", "note"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "note": forms.TextInput(attrs={"placeholder": "e.g. Zomato, Cab, Salary..."}),
        }
