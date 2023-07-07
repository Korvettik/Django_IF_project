from django.shortcuts import render

# Create your views here.

# Функции = контроллеры = вьюхи
# Контроллеры можно описать функциями, можно классами

# ОТКУДА БЕРЕТСЯ request ? -----------------------
def index(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')
