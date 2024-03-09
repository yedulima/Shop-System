from django import forms
from .models import Clients

class LoginForms(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['email', 'password']