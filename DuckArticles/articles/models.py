import os

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .imageStorage import OverwriteStorage


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('block-images', filename)


class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True)
    file_html = models.FileField(upload_to='articles/html/', blank=True)

    def __str__(self):
        return self.name


class ArticleBlock(models.Model):
    article = models.ForeignKey(Article, related_name='%(class)s', on_delete=models.CASCADE)
    type = models.CharField(max_length=25)

    class Meta:
        abstract = True


class ImageBlock(ArticleBlock):
    image = models.ImageField(max_length=500, upload_to=get_file_path, storage=OverwriteStorage(), blank=True)

    directory_string_var = 'block-images'


class TextBlock(ArticleBlock):
    description = models.TextField(max_length=1000)
