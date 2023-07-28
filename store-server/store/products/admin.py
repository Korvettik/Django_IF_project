from django.contrib import admin

# Register your models here.
from products.models import Product, ProductCategory, Basket


# admin.site.register(Product)
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # общее перечисление объектов и их поля
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')  # конкретный объект и его поля
    readonly_fields = ('description',)  # какие поля конкретного объекта только на чтение
    search_fields = ('name',)  # поля по которым идет поиск вводимого
    ordering = ('name',)  # поле сортировки в отображении list_display (а в обратном порядке '-name',))

class BasketAdmin(admin.TabularInline):  # делаем спец класс для сбора всех корзин одного пользователя
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)  # поле нельзя менять, только на чтение, иначе ругаться будет
    extra = 0  # сколько пустых корзин показывать
