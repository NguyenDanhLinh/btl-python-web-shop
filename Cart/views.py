import venv
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse
from User.models import User
# Create your views here.
from Product.models import *
from cart.cart import Cart
from . models import Cart as Carts


# @login_required(login_url='/login')
def add_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    category = Category.objects.all()
    cart = request.session.get('cart')
    total_amount = 0
    for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total_amount += a * b
    vat = total_amount*0.2
    total = total_amount+2+vat
    context = {
        'category': category,
        'total_amount': total_amount,
        'vat': vat,
        'total': total,
    }
    return render(request, 'queenok/cart_page.html', context)


# @login_required(login_url='/login')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    category = Category.objects.all()
    cart = request.session.get('cart')
    total_amount = 0
    for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total_amount += a * b
    vat = total_amount*0.2
    total = total_amount+2+vat
    context = {
        'category': category,
        'total_amount': total_amount,
        'vat': vat,
        'total': total,
    }
    return render(request, 'queenok/cart_page.html', context)


# @login_required(login_url='/login')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    category = Category.objects.all()
    cart = request.session.get('cart')
    total_amount = 0
    for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total_amount += a * b
    vat = total_amount*0.2
    total = total_amount+2+vat
    context = {
        'category': category,
        'total_amount': total_amount,
        'vat': vat,
        'total': total,
    }
    return render(request, 'queenok/cart_page.html', context)


# @login_required(login_url='/login')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    category = Category.objects.all()
    cart = request.session.get('cart')
    total_amount = 0
    for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total_amount += a * b
    vat = total_amount*0.2
    total = total_amount+2+vat
    context = {
        'category': category,
        'total_amount': total_amount,
        'vat': vat,
        'total': total,
    }
    return render(request, 'queenok/cart_page.html', context)


# @login_required(login_url='/login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'queenok/cart_page.html')


# @login_required(login_url='/login')
def cart_page(request):
    current_user = request.user
    category = Category.objects.all()
    cart = request.session.get('cart')
    total_amount = 0
    for i in cart:
            a = (int(cart[i]['price']))
            b = (int(cart[i]['quantity']))
            total_amount += a * b
    vat = total_amount*0.2
    total = total_amount+2+vat
    context = {
        'category': category,
        'total_amount': total_amount,
        'vat': vat,
        'total': total,
    }
    return render(request, 'queenok/cart_page.html', context)