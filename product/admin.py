from django.contrib import admin
from product.models import Product, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'content']
    list_display_links = ['product']
    list_filter = ['product', 'content']


    class Meta:
        model = Comment


admin.site.register(Product)
admin.site.register(Comment, CommentModelAdmin)
