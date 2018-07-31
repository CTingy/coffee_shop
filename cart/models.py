from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from account.models import User
from product.models import Product


PAY_CHOICES = (
    ('面交自取', '面交自取'),
    ('超商取貨付款', '超商取貨付款'),
)

ORDER_STATUS_CHOICES = (
    ('新建立', '新建立'),
    ('已寄出', '已寄出'),
    ('退貨', '退貨'),
)


class OrderManager(models.Manager):
    def new_or_get(self, request):
        order_id = request.session.get("order_id", None)
        qs = self.get_queryset().filter(id=order_id)
        if qs.exists():
            is_new = False
            order_obj = qs.first()
            if request.user.is_authenticated and order_obj.user is None:
                order_obj.user = request.user
                order_obj.save()
        else:
            order_obj = Order.objects.new(user=request.user)
            is_new = True
            request.session['order_id'] = order_obj.id
        return order_obj, is_new

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    subtotal = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    pay = models.CharField(default='', choices=PAY_CHOICES, max_length=120)
    timestamp = models.DateTimeField(null=True, blank=True)
    status = models.CharField(default='新建立', choices=ORDER_STATUS_CHOICES, max_length=120)
    done = models.BooleanField(default=False)

    objects = OrderManager()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('cart:order_read', kwargs={'order_id': self.id})

    class Meta:
        ordering = ['-id', ]


def pre_save_order_total(sender, instance, *args, **kwargs):
    instance.subtotal = sum([cart.total for cart in instance.carts.all()])
    instance.total = instance.subtotal + instance.shipping


pre_save.connect(pre_save_order_total, sender=Order)


class CartManager(models.Manager):
    def new_or_get(self, request, order_obj, product):
        qs = self.get_queryset().filter(product=product, order=order_obj)
        if qs.exists():
            cart_obj = qs.first()
            cart_obj.quantity += 1
            cart_obj.save()
        else:
            cart_obj = self.model.objects.create(product=product, order=order_obj)
        # request.session['cart_items'] = sum([cart.quantity for cart in order_obj.carts.all()])
        return cart_obj


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='carts', default=None)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id', ]


def pre_save_cart_total(sender, instance, *args, **kwargs):
    instance.total = instance.product.price * instance.quantity


pre_save.connect(pre_save_cart_total, sender=Cart)
