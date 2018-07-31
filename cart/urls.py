from django.urls import path

from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_cart, name='add'),
    path('delete/<int:cart_id>/', views.delete_cart, name='delete'),
    path('update/<int:cart_id>/', views.update_cart, name='update'),
    path('update_order/', views.update_order, name='update_order'),
    path('check_order/', views.check_order, name='check_order'),
    path('check_done/', views.check_done, name="check_done"),
    path('orders/', views.order_home, name='orders'),
    path('order/<int:order_id>', views.order_read, name='order_read'),
    path('order_delete/<int:order_id>', views.order_delete, name='order_delete')
]
