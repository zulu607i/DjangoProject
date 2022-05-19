from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    TYPE = (
        ('Sell', 'Sell'),
        ('Buy', 'Buy'),
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    post_type = models.CharField(max_length=150, null=True, choices=TYPE)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title