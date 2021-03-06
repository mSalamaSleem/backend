from django.utils.text import slugify
from django.db import models
from shops.models import SubCategory, Category

class Product(models.Model):
    Title = models.CharField(max_length=30)
    price = models.IntegerField(default=100)
    description = models.CharField(max_length=200)
    discount = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    img = models.ImageField(upload_to='images', default="cloud.jpg", null=True, blank=True)
    stock = models.IntegerField(default=10)
    subcategory = models.ForeignKey(SubCategory, default=1, on_delete=models.CASCADE, related_name="products")

    # product = models.ManyToManyField(Order, on_delete=models.CASCADE, related_name='product_ordered')

    def __str__(self):
        return self.Title

    def __repr__(self):
        return self.Title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title)
        super(Product, self).save(*args, **kwargs)


# class Order(models.Model):
#     code = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     slug = models.SlugField(blank=True, null=True)
#
#     def __str__(self):
#         return self.code
#
#     def __repr__(self):
#         return self.code
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.code)
#         super(Order, self).save(*args, **kwargs)

#
# class ProductOrder(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ordered')
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product_ordered')
#
#     def __str__(self):
#         return f'order with code{self.order.code} has product {self.product.Title}'
#
#     def __repr__(self):
#         return f'{self.order.code}'
#
#
# class Delivery_Person(models.Model):
#     name = models.CharField(max_length=20)
#     phone = models.CharField(max_length=12)
#     slug = models.SlugField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Delivery_Person, self).save(*args, **kwargs)
