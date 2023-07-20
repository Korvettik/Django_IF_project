from django import  forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'Введите пароль'}))
    class Meta:
        model = User  # указываем модель-строку из бд
        fields = ('username', 'password')  # какие поля берем для обработки, кортеж, можно список
