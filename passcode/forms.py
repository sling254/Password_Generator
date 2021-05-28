from django import forms
from .models import PasswordGenearator

class  PasswordGeneratorForm(forms.ModelForm):
    class Meta:
        model = PasswordGenearator
        fields = ("__all__")