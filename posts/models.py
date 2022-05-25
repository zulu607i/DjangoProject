from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from products.models import Product

class Post(models.Model):
    TYPE = (
        ('Sell', 'Sell'),
        ('Buy', 'Buy'),
    )
    STATUS = (
        ('Active', 'Active'),
        ('Closed', 'Closed'),
        ('Incomplete',  'Incomplete')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    post_type = models.CharField(max_length=150, null=True, choices=TYPE)
    assigned_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL,)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=150, null=True, choices=STATUS)

    def __str__(self):
        return self.title