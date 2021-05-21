from rest_framework import serializers
from article.models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "author")

        