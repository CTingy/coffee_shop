from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product, name='product'),
    path('create_product/', views.create_product, name='create_product'),
    path('read_product/<int:product_id>/', views.read_product, name='read_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('search_product/', views.search_product, name='search_product'),
    path('create_comment/<int:product_id>/', views.create_comment, name='create_comment'),
    # path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
