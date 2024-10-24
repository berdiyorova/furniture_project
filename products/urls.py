from django.urls import path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('list/category/<int:category_id>/', ProductListView.as_view(), name='list'),
]
