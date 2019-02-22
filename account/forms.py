from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_two = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password_two(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_two']:
            raise forms.ValidationError('两次输入密码不一致！')
        return cd['password_two']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')

