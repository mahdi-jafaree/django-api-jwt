from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializer import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.post_objects.all()
    serializer_class = PostSerializer
