from dataclasses import fields
from django import forms
from .models import CrudModel

class CrudForm(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = [
            'title',
            'description',
        ]
