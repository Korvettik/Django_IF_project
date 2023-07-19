from django.shortcuts import render

from users.models import User
from users.forms import UserLoginForm

def login(request):
    context = {'form': UserLoginForm()}  # передаем по ключу и вызываем
    return render(request, 'users/login.html', context)


def registration(request):
    return render(request, 'users/registration.html')
