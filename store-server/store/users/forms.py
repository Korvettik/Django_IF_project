from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User  # указываем модель-строку из бд
        fields = ('username', 'password')  # какие поля берем для обработки, кортеж, можно список
