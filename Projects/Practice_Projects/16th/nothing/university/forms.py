from django import forms
from .models import University

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']
        
    # established = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'])