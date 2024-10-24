from django.urls import path

from products.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('list/category/<int:category_id>/', ProductListView.as_view(), name='list'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='detail'),
]
