from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from news.models import News, Comment
from news.serializers import NewsSerializer, NewsListSerializer, CommentSerializer


class NewsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return News.objects.filter(~Q(usernews__user=self.request.user))


class FavoriteNewsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return News.objects.filter(usernews__user=self.request.user, usernews__liked=True)


class ReadNewsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsListSerializer

    def get_queryset(self):
        return News.objects.filter(usernews__user=self.request.user, usernews__read=True)

class NewsDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'pk'


class CommentCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        news_id = self.kwargs['pk']
        return Comment.objects.filter(news_id=news_id)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = 'pk'
