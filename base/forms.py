from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admission_number', 'name', 'unit', 'date']  
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  
        }
