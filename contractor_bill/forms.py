from django import forms
from .models import ContractorBill
class ContractorBillForm(forms.ModelForm):
    class Meta:
        model = ContractorBill
        fields = [
            'name_of_project',
            'type_of_project',
            'name_of_work',
            'work_unit',
            'name_of_contractors_company',
            'quantity',
            'unit_rate'
        ]
        widgets = {
            'type_of_project': forms.Select(choices=ContractorBill.TYPE_CHOICES),
            'work_unit': forms.Select(choices=ContractorBill.WORK_UNIT_CHOICES),
        }
