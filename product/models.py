from django.urls import reverse
from django.db import models
from account.models import User

import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)  # '123.jpg'
    name, ext = os.path.splitext(base_name)  # ('123', '.jpg')
    return name, ext


def upload_image_path(instance, filename):
    # print(instance.title) -> model instance name
    new_filename = random.randint(1, 2323524012)
    name, ext = get_filename_ext(filename)
    final_filename = '{}{}'.format(new_filename, ext)
    return 'product/{}'.format(final_filename)


class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=300)
    image = models.ImageField(upload_to=upload_image_path, default='product/2238217906.jpg', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:read_product', kwargs={'product_id': self.id})


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_time']

    def __str__(self):
        return self.product.title + '-' + str(self.id)

