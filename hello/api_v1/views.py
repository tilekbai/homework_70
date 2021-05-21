from rest_framework import generics, serializers

from article.models import Article
from .serializers import ArticlesListSerializer

class ArticleListView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    queryset = Article.objects.all()