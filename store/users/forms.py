from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)
from users.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите имя'
    }))

    last_name = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите фамилию'
    }))

    username = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'
    }))

    email = forms.CharField(max_length=50, widget=forms.EmailInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите адрес эл. почты'
    }))

    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'
    }))

    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput({
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль еще раз'
    }))
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        }

class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
    }))
    image = forms.ImageField(max_length=50, widget=forms.FileInput({
        'class': 'custom-file-input',
        'required': False
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control py-4',
        'readonly': True
    }))
    email = forms.CharField(max_length=50, widget=forms.EmailInput({
        'class': 'form-control py-4',
        'readonly': True
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']
