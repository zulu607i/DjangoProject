from django import forms
from .models import Post
from products.models import Product

class PostCreate(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_product'].queryset = Product.objects.filter(user=user)

    class Meta:
        model = Post
        fields = [
            'title',
            'post_type',
            'description',
            'status',
            'assigned_product',
        ]