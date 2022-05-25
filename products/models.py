from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Product(models.Model):
    CATEGORY = (
        ('Electronics', 'Electronics'),
        ('Fashion', 'Fashion'),
        ('Furniture', 'Furniture'),
        ('Sports', 'Sports'),
        ('Pets', 'Pets'),
        ('Jewelry', 'Jewelry'),
    )
    USAGE_STATUS = (
        ('Brand New', 'Brand New'),
        ('Almost New', 'Almost New'),
        ('Gently New', 'Gently New'),
        ('Havely New', 'Havely New'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    product_name = models.CharField(max_length=150, null=True)
    description = models.TextField(max_length=150, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, choices=CATEGORY)
    usage_status = models.CharField(max_length=150, null=True, choices=USAGE_STATUS)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')
    brand = models.CharField(max_length=100, null=True, blank=True, verbose_name='Brand')
    location = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location')
    model_type = models.CharField(max_length=100, null=True, blank=True, verbose_name='Model')
    price = models.FloatField(null=True)

    def __str__(self):
        return self.product_name