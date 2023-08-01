from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import ProductCategory, Product, Basket
from users.models import User
from django.core.paginator import Paginator

# Create your views here.

# Функции = контроллеры = вьюхи
# Контроллеры можно описать функциями, можно классами

# ОТКУДА БЕРЕТСЯ request ------ это объект входного потока данных HTMLResponse

class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context

# def index(request):
#     context = {'title': 'Store'}
#     return render(request, 'products/index.html', context)





class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):   # переопределяем получение списка объектов с применением фильтра
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):  # задаем контекст
        context = super(ProductsListView, self).get_context_data()
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context




# def products(request, category_id=None, page_number=1):
#     if category_id:  # добавляем фильтрацию выбранной категории, если есть в теле запроса
#         category = ProductCategory.objects.get(id=category_id)
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()
#
#     per_page = 3  # число товаров на странице
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#
#     context= {
#         'title': 'Store - Каталог',
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all()
#     }
#     return render(request, 'products/products.html', context)







@login_required  # специальный декоратор, чтобы не было возможности
# добавить в корзину товар неавторизованному пользователю
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])   # возвращает тот путь той страницы, где находимся сейчас






@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])