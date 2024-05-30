from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Customer, Product, Category

def main_page(request):
    template = 'main.html'
    product = Product.objects.all()

    context = {
        'user': request.user,
        'product': product,
    }
    return render(request, template, context=context)


def product_info(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        'product': product,
        'availability': 'w magazynie' if product.in_stock else 'brak w magazynie',
    }
    return render(request, 'product.html', context=context)

def categories(request, foo):
    foo = foo.replace("-", " ")
    try:
        category = Category.objects.get(name=foo)
        product = Product.objects.filter(category=category)

        context = {
            "category": category,
            "products": product,
        }
        return render(request, 'categories.html', context=context)

    except:
        messages.info(request, 'Category is not found!!!')
        return redirect('main')
