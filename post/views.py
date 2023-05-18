from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from .filters import PostFilter


# Create your views here.
class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
