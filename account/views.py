from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from account.forms import UserForm
from cart.views import update_cart_items


def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'form': UserForm()})

    # POST
    form = UserForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form': form})
    form.save()
    messages.success(request, '歡迎註冊，請登入')
    return redirect('product:product')


def login(request):
    '''
    Login an existing user
    '''
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template, {'next_url': request.GET.get('next')})

    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)
    # login success
    auth_login(request, user)
    next_url = request.POST.get('next_url')
    if next_url:
        return redirect(next_url)
    messages.success(request, '登入成功，請參觀我的賣場')
    orders = user.orders.filter(done=False)
    if orders.exists() and not request.session.get('order_id'):
        request.session['order_id'] = orders.last().id
        update_cart_items(request)
    return redirect('product:product')


@login_required
def logout(request):
    '''
    Logout the user
    '''
    auth_logout(request)
    messages.success(request, '登出成功，歡迎再度光臨')
    return redirect('product:product')


@login_required
def profile(request):
    return render(request, 'account/profile.html', {'user': request.user})
