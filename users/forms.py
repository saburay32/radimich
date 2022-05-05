# ----------------------
#   Code by Radimich   
#   Date: 2022          
#   Land:Larnevsk     
# ----------------------
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']