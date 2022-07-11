from django.contrib import admin
from .customer import Customer
from .category import Category
from .products import Product
from .orders import Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'phone')


class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','customer', 'address')


admin.site.register(Order, OrderAdmin)


admin.site.register(Category, CategoryAdmin)


admin.site.register(Customer, CustomerAdmin)





