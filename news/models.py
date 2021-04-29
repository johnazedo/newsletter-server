from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=512)
    text = models.TextField()
    author = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    # likes = models.IntegerField(default=0)
    # qComments = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    @property
    def number_comments(self):
        return Comment.objects.filter(news_id=self.id).count()

    @property
    def number_likes(self):
        return UserNews.objects.filter(news_id=self.id).count()

    # def save(self, **kwargs):
    #     self.likes = UserNews.objects.filter(news=self.id).count()
    #     self.comments = Comment.objects.filter(news=self.id).count()
    #     super(News, self).save(**kwargs)


class UserNews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'UserNews'
        verbose_name_plural = 'UserNews'

    def __str__(self):
        return f'{self.user.first_name} - {self.news.title}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at', 'pk']

    def __str__(self):
        return f'{self.user.first_name} - {self.news.title}'

