from django.shortcuts import render
from .models import Author, Blog, Comment
from .serializers import AuthorSerializer, BlogSerializer, CommentSerializer
from rest_framework import viewsets

# Create your views here.


class AuthorList(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogList(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentList(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
