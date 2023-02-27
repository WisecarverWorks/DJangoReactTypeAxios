from django import forms
from .models import Car


class CarUploadForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'picture', 'thumbnail']
