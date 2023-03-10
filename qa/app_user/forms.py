from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import MyUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class MyUserCreatingForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
            model = MyUser
            fields = ('username', 'password1', 'password2', 'email',)

