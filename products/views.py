from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, BrandModel, ColorModel, SizeModel, TagModel, ProductImageModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    @staticmethod
    def get_colors():
        colors = ColorModel.objects.all()
        new_colors = list()
        temp_color = list()

        for color in colors:
            if len(temp_color) == 2:
                new_colors.append(temp_color)
                temp_color.clear()
            else:
                temp_color.append(color)

        if temp_color:
            new_colors.append(temp_color)

        return new_colors

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['parents'] = CategoryModel.objects.filter(parent=None)
        context['categories'] = CategoryModel.objects.exclude(parent=None)
        context['category'] = get_object_or_404(CategoryModel, id=self.kwargs['category_id'])

        context['tags'] = TagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = self.get_colors()
        context['sizes'] = SizeModel.objects.all()
        return context

    def get_queryset(self):
        # Get the category from the URL parameters
        category_id = self.kwargs['category_id']
        category = CategoryModel.objects.filter(id=category_id).first()

        order = self.request.GET.get('order')

        if category.parent is None:
            queryset = ProductModel.objects.filter(categories__in=category.children.all()).distinct()
        else:
            queryset = ProductModel.objects.filter(categories=category)

        if order == 'name_asc':
            products = queryset.order_by('name')
        elif order == 'name_desc':
            products = queryset.order_by('-name')
        elif order == 'price_asc':
            products = queryset.order_by('real_price')
        elif order == 'price_desc':
            products = queryset.order_by('-real_price')
        else:
            products = queryset.order_by('-created_at')

        return products


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImageModel.objects.filter(product=ProductModel.objects.get(id=self.kwargs['pk']))
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     pk = self.kwargs.get('pk')
    #     cat_id = self.kwargs.get('cat_id')
    #
    #     return queryset.objects.filter()
