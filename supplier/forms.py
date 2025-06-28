from django import forms
from .models import Supplier
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name_of_supplier', 'supplier_address', 'supplier_contact_no']
        labels = {
            'name_of_supplier': 'Supplier Name',
            'supplier_address': 'Supplier Address',
            'supplier_contact_no': 'Contact Number',
        }
        widgets = {
            'name_of_supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter supplier name'}),
            'supplier_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'supplier_contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
        }
