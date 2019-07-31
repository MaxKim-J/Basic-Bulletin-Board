from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.list_article, name='list'),
    path('create/', views.create_article, name='create'),
    path('<int:pk>/', views.detail_article, name='detail'),
    path('tags/<int:pk>', views.tags_article, name='tags')
]
