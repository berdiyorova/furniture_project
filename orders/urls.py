from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('cart/<int:pk>/', views.add_or_remove, name='add-or-remove'),
    path('wishlist/<int:pk>/', views.product_in_wishlist, name='in-wishlist'),
]
