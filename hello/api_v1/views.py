from rest_framework import generics, serializers

from article.models import Article
from .serializers import *

class ArticleListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()