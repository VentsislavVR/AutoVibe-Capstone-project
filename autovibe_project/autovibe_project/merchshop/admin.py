from django.contrib import admin

from autovibe_project.merchshop.models import Product, CartItem

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass