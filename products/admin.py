from django.contrib import admin
from .models import Product
from .models import CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
