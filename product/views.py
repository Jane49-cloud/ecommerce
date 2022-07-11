from django.shortcuts import render
from .products import Product
from .category import Category


def index(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categorys': categorys})


def single_category(category_id):
    if category_id:
        products = Product.objects.filter(category=category_id)
        return render('single-category.html', {'products': products})
    else:
        products = Product.get_all_products()
        return render('index.html', {'products': products})


def get_all_products():
    return Product.objects.all()
