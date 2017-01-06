from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.views.generic import View
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

from .forms import AddUserForm, LoginForm
from .models import Product, Category

# categories for every view nav bar
categories = Category.objects.all()


class Index(View):
    """View for showing catalogs in index page"""
    form_class = LoginForm
    template = 'catalog/login-modal.html'

    def get(self, request):
        username = user_name(request)
        form = self.form_class(None)
        context = {
            'form': form,
            'username': username,
            'categories': categories,
        }
        return render(request, 'catalog/home.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            form = self.form_class(None)
            context = {
                'form': form,
                'username': username,
                'categories': categories,
            }
            return render(request, 'catalog/home.html', context)
        else:
            return HttpResponse('wrong username or password')


# @login_required
def product_view(request, category_name, category_id):
    """View for showing all products of a given category"""
    names = [c.name for c in Category.objects.all()]
    if category_name not in names:
        template = loader.get_template('catalog/404Page.html')
        return HttpResponseNotFound(template.render(request))
    else:
        username = user_name(request)
        products = Product.objects.filter(categories=category_id)
        context = {
            'username': username,
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
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # login right away
            return HttpResponseRedirect(reverse('index'))  # redirect to home page
        else:
            return HttpResponse('Data not valid')


def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')  # redirects to home


def user_name(request):
    return 'anonimo' if request.user.is_anonymous() else request.user.get_username()
