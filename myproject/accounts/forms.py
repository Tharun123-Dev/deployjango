from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
 password = forms.CharField(widget=forms.PasswordInput, label='Password')
 password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')


 class Meta:
  model = User
  fields = ['username', 'email']


  def clean(self):
   cleaned = super().clean()
   pw = cleaned.get('password')
   pw2 = cleaned.get('password2')
   if pw and pw2 and pw != pw2:
    raise forms.ValidationError('Passwords do not match')
   return cleaned


class LoginForm(forms.Form):
 username = forms.CharField(max_length=150)
 password = forms.CharField(widget=forms.PasswordInput)