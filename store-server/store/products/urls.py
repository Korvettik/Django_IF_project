from django.urls import path
from products.views import products  #ничего страшного, что подсвечивает

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]
