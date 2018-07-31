from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']
