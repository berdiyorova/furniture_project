from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect(reverse('products:list', kwargs={'category_id': 1}))


def product_in_wishlist(request, pk):
    wishlist = request.session.get('wishlist', [])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)

    request.session['wishlist'] = wishlist
    return redirect(reverse('products:list', kwargs={'category_id': 1}))
