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
