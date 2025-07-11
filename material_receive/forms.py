from django import forms
from .models import MaterialReceive
from material.models import Material

class MaterialReceiveForm(forms.ModelForm):
    class Meta:
        model = MaterialReceive
        fields = [
            'project_name',
            'material_name',
            'unit',
            'material_type',
            'material_group',
            'receive_date',
            'channel_no',
            'receive_quantity',
        ]
        widgets = {
            'project_name': forms.Select(attrs={
                'class': 'form-control',
            }),
            'material_name': forms.Select(attrs={
                'class': 'form-control',
            }),
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from material',
            }),
            'material_type': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from material',
            }),
            'material_group': forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder': 'Auto-filled from material',
            }),
            'receive_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'channel_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Channel No',
            }),
            'receive_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        material = cleaned_data.get('material_name')

        # ✅ Safely assign values to the instance, not cleaned_data
        if material:
            self.instance.unit = material.material_unit
            self.instance.material_type = material.type_of_material
            self.instance.material_group = material.group_of_material

        return cleaned_data




