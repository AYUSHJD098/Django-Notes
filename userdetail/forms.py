from django.forms import ModelForm, TextInput, Textarea
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserResgisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': "form-control", "placeholder":"Username", "type":"text"}),
            'email': TextInput(attrs={"class":"form-control", "placeholder":"Email address", "type":"email"}),
            'password1': TextInput(attrs={"class":"form-control", "placeholder":"Password", "type":"password"}),
            'password2': TextInput(attrs={"class":"form-control", "placeholder":"Confirm Password", "type":"password"}),
        }
 
