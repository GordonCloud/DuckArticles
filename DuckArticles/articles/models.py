import os

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True)
    file_html = models.FileField(upload_to='articles/html/', blank=True)

    def __str__(self):
        return self.name


class ArticleBlock(models.Model):
    article = models.ForeignKey(Article, related_name='%(class)s', on_delete=models.SET_NULL, null=True, blank=True)
    priority = models.IntegerField(null=True)

    class Meta:
        abstract = True


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.type, instance.article, ext)
    return os.path.join('block-images', filename)


class ImageBlock(ArticleBlock):
    image = models.ImageField(max_length=500, upload_to=get_file_path, blank=True)


class TextBlock(ArticleBlock):
    description = models.TextField(max_length=1000)


class TinyMCEBlock(ArticleBlock):
    content = models.TextField()
    