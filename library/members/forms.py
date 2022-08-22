from django import forms
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Last Name'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class MemberForm(forms.ModelForm):
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Phone Number'}))
    birthdaydate=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control my-2','placeholder':'Birthday'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Address'}))
    class Meta:
        model = Member
        fields = ('phone', 'birthdaydate', 'address')
