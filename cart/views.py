from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from datetime import datetime

from product.models import Product
from .models import Cart, Order
from .forms import OrderForm
from contact.views import send_mail


def update_cart_items(request):
    order_obj, is_new = Order.objects.new_or_get(request)
    count = sum([cart.quantity for cart in order_obj.carts.all()])
    request.session['cart_items'] = count
    return count


def home(request):
    order_obj, is_new = Order.objects.new_or_get(request)
    return render(request, 'cart/cart.html', {'order': order_obj})


def add_cart(request):
    if request.method == 'GET':
        return redirect('product:product')
    # POST
    order_obj, is_new = Order.objects.new_or_get(request)
    product_id = request.POST.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    cart_obj = Cart.objects.new_or_get(request, order_obj, product)
    count = update_cart_items(request)
    if request.is_ajax():
        json_data = {'cartItemCount': count}
        return JsonResponse(json_data)
    return redirect('cart:home')


def update_cart(request, cart_id):
    if request.method == 'GET':
        return redirect('cart:home')
    # POST
    cart_obj = get_object_or_404(Cart, id=cart_id)
    cart_obj.quantity = int(request.POST.get('quantity'))
    cart_obj.save()
    count = update_cart_items(request)
    if request.is_ajax():
        json_data = {'cartItemCount': count, 'cartTotal': cart_obj.total}
        return JsonResponse(json_data)
    return redirect('cart:home')


def delete_cart(request, cart_id):
    cart_obj = get_object_or_404(Cart, id=cart_id)
    cart_obj.delete()
    count = update_cart_items(request)
    if request.is_ajax():
        json_data = {'cartItemCount': count}
        return JsonResponse(json_data)
    return redirect('cart:home')


@login_required
def update_order(request):
    order_obj, is_new = Order.objects.new_or_get(request)
    # GET
    if request.method == 'GET':
        if request.GET.get('shop'):
            order_obj.shipping = 70
            order_obj.pay = '超商取貨付款'
            order_obj.save()
        elif request.GET.get('self'):
            order_obj.shipping = 0
            order_obj.address = '自取'
            order_obj.pay = '面交自取'
            order_obj.save()
        form = OrderForm(instance=order_obj)
        return render(request, 'order/order_form.html', {'form': form, 'order': order_obj})
    # POST
    form = OrderForm(request.POST, instance=order_obj)
    if not form.is_valid():
        return render(request, 'order/order_form.html', {'form': form, 'order': order_obj})
    order_obj.address = request.POST.get('stName')
    form.save()
    return redirect('cart:check_order')


@login_required
def check_order(request):
    order_obj, is_new = Order.objects.new_or_get(request)
    form = OrderForm(instance=order_obj)
    if request.method == 'GET':
        return render(request, 'order/check_order.html', {'form': form, 'order': order_obj})
    order_obj.done = True
    order_obj.timestamp = datetime.now()
    order_obj.save()
    return redirect('cart:check_done')


@login_required
def check_done(request):
    order_obj, is_new = Order.objects.new_or_get(request)
    # send_mail(mail=order_obj.user.email)
    del request.session['order_id']
    del request.session['cart_items']
    return render(request, 'order/check_done.html', {'order': order_obj})


@login_required
def order_home(request):
    orders = Order.objects.filter(user=request.user).filter(done=True)
    return render(request, 'order/order_home.html', {'orders': orders})


@login_required
def order_read(request, order_id):
    order_obj = get_object_or_404(Order, id=order_id)
    return render(request, 'order/order_read.html', {'order': order_obj})


@login_required
def order_delete(request, order_id):
    if request.method == 'GET':
        return order_home(request)
    order_obj = get_object_or_404(Order, id=order_id)
    order_obj.delete()
    messages.success(request, '訂單已刪除')
    return redirect('cart:orders')
