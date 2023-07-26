from django.db import models
from users.models import User

# Create your models here.
class ProductCategory(models.Model):
    # id создается по умолчанию
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)  # не обязательно к заполнению

    def __str__(self):
        return self.name



class Product(models.Model):
    # id создается по умолчанию
    name = models.CharField(max_length=256)
    description = models.TextField()   # обязательно к заполнению
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'Продукт: {self.name}, Категория: {self.category.name}'


class Basket(models.Model):
    # id создается по умолчанию
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)  # автоматически заполняется

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'
