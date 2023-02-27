from django import forms
from .models import Employee


class EmployeeUploadForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'picture', 'thumbnail']
