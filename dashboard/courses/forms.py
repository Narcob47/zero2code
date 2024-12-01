from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

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

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your first name',
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your last name',
        })
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your address',
        })
    )
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
        })
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'address', 'profile_picture']

class UserForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your email',
        })
    )

    class Meta:
        model = User
        fields = ['email']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your old password',
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Enter your new password',
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 mt-2 text-gray-700 bg-gray-50 border rounded-lg focus:ring focus:ring-blue-300 focus:border-blue-400 focus:outline-none',
            'placeholder': 'Confirm your new password',
        })
    )