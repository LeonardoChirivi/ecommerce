from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template import loader

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
    names = [c.name for c in Category.objects.all()]
    if category_name not in names:
        template = loader.get_template('catalog/404Page.html')
        return HttpResponseNotFound(template.render(request))
    else:
        products = Product.objects.filter(categories=category_id)
        context = {
            'category': category_name,
            'products': products,
        }
        return render(request, 'catalog/product.html', context)
