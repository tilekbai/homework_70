from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView,
)

app_name = 'api_v1'

urlpatterns = [
    path('all/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
]