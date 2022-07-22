from django.shortcuts import render, get_object_or_404
from .products import Product
from .category import Category


def index(request):
    # category = None
    categorys = Category.objects.all()
    products = Product.objects.all()
    # if category_slug:
    #     category = get_object_or_404(category, slug=category_slug)
    #     products = Product.filter(category=category)
    return render(request, 'index.html', {'products': products,
                                          'categorys': categorys})


def category_products(request, pk):
    category = Category.objects.get(pk=pk)
    if pk:
        product = Product.objects.filter(category=pk)
    else:
        product = Product.objects.all()
    return render(request, 'single_category.html', {'category': category, 'product': product})
