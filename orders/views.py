from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView

from products.models import ProductModel


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


class UserCartView(ListView):
    template_name = 'ordering/cart.html'
    context_object_name = 'products'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.objects.filter(id__in=cart)
