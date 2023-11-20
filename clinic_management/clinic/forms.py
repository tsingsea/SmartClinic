# clinic/forms.py

from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'
        widgets = {
            'record_date': forms.DateInput(attrs={'type': 'date'}),
        }
