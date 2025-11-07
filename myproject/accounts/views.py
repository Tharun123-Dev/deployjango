from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm




def index(request):
 return render(request, 'index.html')

 


def register_view(request):
 if request.method == 'POST':
   form = RegisterForm(request.POST)
   if form.is_valid():
     user = form.save(commit=False)
     user.set_password(form.cleaned_data['password'])
     user.save()
     messages.success(request, 'Registration successful. You can now log in.')
     return redirect('login')
 else:
   form = RegisterForm()
 return render(request, 'register.html', {'form': form})




def login_view(request):
  if request.method == 'POST':
   form = LoginForm(request.POST)
   if form.is_valid():
     username = form.cleaned_data['username']
     password = form.cleaned_data['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:
       login(request, user)
       messages.success(request, 'Login successful! Welcome, {}.'.format(user.username))
       return redirect('success')
     else:
       messages.error(request, 'Invalid credentials')
  else:
     form = LoginForm()
  return render(request, 'login.html', {'form': form})




def success_view(request):
# Simple protected page that shows a success message
 if not request.user.is_authenticated:
  messages.error(request, 'You must log in first')
  return redirect('login')
 return render(request, 'success.html')




def logout_view(request):
 logout(request)
 messages.info(request, 'You have logged out.')
 return redirect('index')