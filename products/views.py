from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, CategoryModel, BrandModel, ColorModel, SizeModel, TagModel


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
        products = list()

        if category.parent is None:
            for cat in category.children.all():
                products += ProductModel.objects.filter(categories=cat)
        else:
            products = ProductModel.objects.filter(categories=category)

        if order == 'name_asc':
            products = products.order_by('name')
        elif order == 'name_desc':
            products = products.order_by('-name')
        elif order == 'price_asc':
            products = products.order_by('real_price')
        elif order == 'price_desc':
            products = products.order_by('-real_price')
        else:
            products = products.order_by('-created_at')

        return products

