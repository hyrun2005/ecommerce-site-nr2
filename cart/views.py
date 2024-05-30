from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    return render(request, 'cart_info.html', {})


def cart_add(request):
    #get the cart
    cart = Cart(request)

    #test for POST
    if request.POST.get('action') == 'post':

        # get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # save to session
        cart.add(product=product)
        cart_quantity = cart.__len__()

        # return a response
        #response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'CartQuantity': cart_quantity})
        return response




def cart_delete(request):
    pass


def cart_refresh(request):
    pass

