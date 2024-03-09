from django import forms
from .models import Users

class LoginForms(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'password']