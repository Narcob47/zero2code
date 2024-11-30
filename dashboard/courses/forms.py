from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your email',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your password',
        })
    )