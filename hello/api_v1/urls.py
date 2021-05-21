from django.urls import path
from .views import (
    ArticleListView,
)

app_name = 'api_v1'

urlpatterns = [
    path('all/', ArticleListView.as_view()),
]