from django.contrib import admin

from .models import Article, ImageBlock, TextBlock

admin.site.register(Article)
admin.site.register(ImageBlock)
admin.site.register(TextBlock)