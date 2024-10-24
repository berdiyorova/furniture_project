from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import AbstractBaseModel


class CategoryModel(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Category name"))
    parent = models.ForeignKey('self',
                               on_delete=models.PROTECT,
                               null=True, blank=True,
                               related_name='children',
                               verbose_name=_("Parent category name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class TagModel(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Tag name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class BrandModel(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Brand name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class ColorModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Color name"))
    code = models.CharField(max_length=255, unique=True, verbose_name=_("Color code"))


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class SizeModel(AbstractBaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Size name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class ProductModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Product name"))
    image1 = models.ImageField(upload_to='products/', verbose_name=_("Image 1"))
    image2 = models.ImageField(upload_to='products/', verbose_name=_("Image 2"))
    short_description = models.TextField(verbose_name=_("Short description"))
    long_description = models.TextField(verbose_name=_("Long description"))
    sku = models.CharField(max_length=10, unique=True)
    is_stock = models.BooleanField(default=True, verbose_name=_("Is stock"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    discount = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Real price"))

    categories = models.ManyToManyField(CategoryModel, related_name='products')
    tags = models.ManyToManyField(TagModel, related_name='products')
    sizes = models.ManyToManyField(SizeModel, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products')

    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def is_discount(self):
        return True if self.discount != 0 else False


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
