from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    body = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Post
        fields = ["body"]
