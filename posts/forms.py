from django import forms
from .models import Post

class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'post_type',
            'description',
        ]