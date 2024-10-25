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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        products = list()
        cart = self.request.session.get('cart', [])
        for product_id in cart:
            products.append(ProductModel.objects.get(id=product_id))

        context['products'] = products
        return context
