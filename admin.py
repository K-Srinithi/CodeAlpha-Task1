from django.contrib import admin
from .models import Product, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    fields = ('name','price','description','image')

from .models import CartItem
admin.site.register(CartItem)
