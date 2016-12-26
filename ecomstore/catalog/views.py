from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import View
# from django.contrib.auth.decorators import login_required

from .forms import AddUserForm
from .models import Product, Category

# categories for every view nav bar
categories = Category.objects.all()


def index(request):
    """View for showing catalogs in index page"""
    context = {
        'categories': categories,
    }
    return render(request, 'catalog/home.html', context)


# @login_required
def product_view(request, category_name, category_id):
    """View for showing all products of a given category"""
    names = [c.name for c in Category.objects.all()]
    if category_name not in names:
        template = loader.get_template('catalog/404Page.html')
        return HttpResponseNotFound(template.render(request))
    else:
        products = Product.objects.filter(categories=category_id)
        context = {
            'categories': categories,  # added
            'category': category_name,
            'products': products,
        }
        return render(request, 'catalog/product.html', context)


class UserFormView(View):
    form_class = AddUserForm
    template = 'catalog/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

        return HttpResponse('ok lol')
