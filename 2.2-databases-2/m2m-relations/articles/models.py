from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
class Scope(models.Model):
    articles = models.ManyToManyField(Article, related_name='orders', through='ArticleScope')

class ArticleScope(models.Model):
    tag = models.CharField(max_length=256, verbose_name='Название')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='positions')
    scopes = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='positions')