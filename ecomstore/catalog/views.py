from django.shortcuts import (render,
                              get_object_or_404,
                              HttpResponse)

from .models import Product, Category


def index(request):
    """View for showing catalogs in index page"""
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'catalog/index.html', context)


def product_view(request, category_name, category_id):
    """View for showing all products of a given category"""
    products = Product.objects.filter(categories=category_id)
    context = {
        'category': category_name,
        'products': products,
    }
    return render(request, 'catalog/product.html', context)
