from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, CategoryModel, BrandModel, ColorModel, SizeModel, TagModel


class ProductListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        parents = context['parents'] = CategoryModel.objects.filter(parent=None)

        categories = list()
        for parent in parents:
            for child in parent.children.all():
                categories.append(child)
        context['categories'] = categories[:5]

        context['category'] = get_object_or_404(CategoryModel, id=self.kwargs['category_id'])
        context['tags'] = TagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        return context

    def get_queryset(self):
        # Get the category from the URL parameters
        category_id = self.kwargs['category_id']
        category = CategoryModel.objects.filter(id=category_id).first()

        if category.parent is None:
            categories = category.children.all()
            products = list()
            for cat in categories:
                products += ProductModel.objects.filter(categories=cat)
            return products

        return ProductModel.objects.filter(categories=category)
