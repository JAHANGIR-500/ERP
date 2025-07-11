from django import forms
from .models import Material
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name_of_material', 'material_unit', 'type_of_material', 'group_of_material']
        labels = {
            'name_of_material': 'Material Name',
            'material_unit': 'Material Unit',
            'type_of_material': 'Type of Material',
            'group_of_material': 'Group of Material',
        }
        widgets = {
            'name_of_material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter material name'}),
            'material_unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter unit'}),
            'type_of_material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter type'}),
            'group_of_material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter group'}),
        }
