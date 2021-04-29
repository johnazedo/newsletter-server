from django.urls import path

from news.views import NewsListView, NewsDetailView, CommentCreateView, CommentDetailView, CommentListView, FavoriteNewsListView, ReadNewsListView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='list-news'),
    path('<int:pk>', NewsDetailView.as_view(), name='detail-news'),
    path('comment', CommentCreateView.as_view(), name='create-comment'),
    path('<int:pk>/comments', CommentListView.as_view(), name='list-comments'),
    path('favorites', FavoriteNewsListView.as_view(), name='favorite-list-news'),
    path('read', FavoriteNewsListView.as_view(), name='read-list-news'),
]
