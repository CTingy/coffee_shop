from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required

from product.models import Product, Comment
from product.forms import ProductForm
from main.views import admin_required


def product(request):
    '''
    Render the product page
    '''
    products = Product.objects.all()
    return render(request, 'product/product.html', {'products': products})


@admin_required
def create_product(request):
    '''
    Create a new product instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the product page
    '''
    template = 'product/create_update_product.html'
    if request.method == 'GET':
        return render(request, template, {'productForm': ProductForm()})

    # POST
    productForm = ProductForm(request.POST)
    if not productForm.is_valid():
        return render(request, template, {'productForm': productForm})
    productForm.save()
    messages.success(request, '商品已新增')
    return redirect('product:product')


def read_product(request, product_id):
    '''
    Read product pages
        1. Get the "product" instance using "product_id"; redirect to the 404 page if not found
        2. Render the read_product template with the product instance and its
           associated comments
    '''
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/read_product.html', {'product': product})


@admin_required
def update_product(request, product_id):
    '''
    Update the article instance:
        ...
    '''
    product = get_object_or_404(Product, id=product_id)
    template = 'product/create_update_product.html'
    if request.method == 'GET':
        productForm = ProductForm(instance=product)
        return render(request, template, {'productForm': productForm})

    # POST
    productForm = ProductForm(request.POST, instance=product)
    if not productForm.is_valid():
        return render(request, template, {'productForm': productForm})
    productForm.save()
    messages.success(request, '商品頁已修改')
    return redirect('product:read_product', product_id=product_id)


@admin_required
def delete_product(request, product_id):
    '''
    Delete the article instance:
        ...
    '''
    if request.method == 'GET':
        return product(request)
    # POST
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, '商品已刪除')
    return redirect('product:product')


def search_product(request):
    '''
    Search for articles:
        ...
    '''
    q = request.GET.get('q')
    qset = q.split()
    products = Product.objects.all()
    for qs in qset:
        products = products.filter(Q(title__icontains=qs) |
                                    Q(content__icontains=qs))
    return render(request, 'search/search_product.html', {'products': products, 'q': q})


@login_required
def create_comment(request, product_id):
    '''
    Create a comment for an article:
        1. Get the "comment" from the HTML form
        2. Store it to database
    '''
    if request.method == 'GET':
        return read_product(request, product_id)

    # POST
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('product:read_product', product_id=product_id)
    product = get_object_or_404(Product, id=product_id)
    Comment.objects.create(product=product, user=request.user, content=comment)
    return redirect('product:read_product', product_id=product_id)


@login_required
def delete_comment(request, comment_id):
    '''
    Delete a comment:
        1. Get the comment to update and its product article; redirect to 404 if not found
        2. Delete the comment
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    product = get_object_or_404(Product, id=comment.product.id)

    if request.method == 'GET':
        return read_product(request, product.id)

    # POST
    if comment.user != request.user:
        messages.error(request, '無刪除權限')
        return redirect('product:read_product', product_id=product.id)

    comment.delete()
    return redirect('product:read_product', product_id=product.id)
