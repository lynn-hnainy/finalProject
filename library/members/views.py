from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, MemberForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
def signin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.get(username=username)
        if user is not None:
            if user.check_password(password):
                return redirect('home')
            else:
                 messages.error(request, 'Username and Password incorrect!')
                 return redirect('login')

        else:
              messages.error(request, 'Username and Password incorrect!')
              return redirect('login')

    else:
        return render(request,'members/login.html')


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        member_form = MemberForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user=user_form.save()
            member=member_form.save(commit=False)
            member.user=user
            member.save()
            messages.success(request, f'Your account was successfully created!')
            return redirect('login')

    else:
        user_form = UserForm()
        member_form = MemberForm()
    return render(request,'members/register.html', {'user_form': user_form,'member_form': member_form})
