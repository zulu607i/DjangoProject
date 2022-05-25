import django_filters
from .models import Post

class PostsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(method='title_filter', label='Title')
    class Meta:
        model = Post
        fields = ['title', 'post_type', 'assigned_product']

    def title_filter(self, queryset, name, value):
        return queryset.filter(title__icontains=value)