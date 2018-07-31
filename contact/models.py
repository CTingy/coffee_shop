from django.db import models

from cart.models import Order


class Contact(models.Model):
    name = models.CharField(max_length=125)
    content = models.TextField()
    order = models.IntegerField(null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id', ]
