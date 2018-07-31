from django.contrib import admin
from django.urls import path, include #re_path
from main import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('product/', include('product.urls', namespace='product')),
    path('board/', include('board.urls', namespace='board')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('contact/', include('contact.urls', namespace='contact')),
    #re_path('.*', views.main),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
