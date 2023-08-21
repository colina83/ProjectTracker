from django import forms
from .models import Status

class StatusUpdateForm(forms.ModelForm):
    date = forms.DateTimeField(
        label='Select Date and Time',
        widget=forms.DateTimeInput(attrs={'class': 'form-control'}),
    )
    
    class Meta:
        model = Status
        fields = ['project', 'status', 'date', 'company']