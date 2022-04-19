# ----------------------
#   Code by Radimich   
#   Date: 2022          
#   Land:Larnevsk     
# ----------------------
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']
