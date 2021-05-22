from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
)

app_name = 'api_v1'

urlpatterns = [
    path('all/', ArticleListView.as_view()),
    path('detail/<int:pk>/', ArticleDetailView.as_view()),
    path('create/', ArticleCreateView.as_view())
] 