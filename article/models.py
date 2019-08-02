from django.db import models
from django_prac4_0730front.models import TimeStampModel


class Article(TimeStampModel):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    delo = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete =models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.author


class Tag(models.Model):
    tag = models.ManyToManyField(Article)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name