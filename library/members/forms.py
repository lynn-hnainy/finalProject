from django import forms
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    email = forms.EmailField()
    # firstname = forms.CharField()
    # lastname = forms.CharField()
    # 'fisrtname','lastname',
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('phone', 'birthdaydate', 'address')
