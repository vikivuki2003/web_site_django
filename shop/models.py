import random
import string

from django.db import models
from django.utils.text import slugify
from django.urls import reverse




class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Category Name')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='children',
                               verbose_name='Parent category')
    slug = models.SlugField(max_length=200, null=False, unique=True, editable=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    @staticmethod
    def rand_slug():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=3))

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'slug')
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rand_slug() + 'between' + self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:category_list', kwargs={'slug': self.slug})

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField("Name", max_length=250)
    brand = models.CharField("Brand", max_length=250)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField('URL', max_length=250)
    price = models.DecimalField(
        "Price", max_digits=7, decimal_places=2, default=99.99)
    image = models.ImageField(
        "Image", upload_to='images/products/%Y/%m/%d', default='products/products/default.jpg')
    available = models.BooleanField("Availability", default=True)
    created_at = models.DateTimeField('Creation date', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Updating date', auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(available=True)


class ProductProxy(Product):

    objects = ProductManager()

    class Meta:
        proxy = True