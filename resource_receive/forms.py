from django import forms
from .models import ResourceReceive

class ResourceReceiveForm(forms.ModelForm):
    class Meta:
        model = ResourceReceive
        fields = ['project_name', 'resource_name', 'unit', 'receive_date', 'channel_no', 'receive_quantity']
        labels = {
            'project_name': 'Project Name',
            'resource_name': 'Resource Name',
            'unit': 'Unit',
            'receive_date': 'Receive Date',
            'channel_no': 'Channel No',
            'receive_quantity': 'Quantity Received',
        }
        widgets = {
            'project_name': forms.Select(attrs={'class': 'form-control'}),
            'resource_name': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'channel_no': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Server-side safeguard: auto-set the unit from selected resource
        in case JavaScript fails or is bypassed.
        """
        cleaned_data = super().clean()
        resource = cleaned_data.get('resource_name')
        if resource:
            cleaned_data['unit'] = resource.resource_unit
        return cleaned_data
