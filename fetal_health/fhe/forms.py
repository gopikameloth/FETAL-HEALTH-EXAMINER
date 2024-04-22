from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'specialisation', 'ph_no', 'hospital_name', 'city', 'password']
