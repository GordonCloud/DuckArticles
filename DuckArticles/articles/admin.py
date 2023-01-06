from django.contrib import admin

from .models import *
from .forms import TinyMCEBlockForm


class TinyMCEBlockAdmin(admin.ModelAdmin):
    form = TinyMCEBlockForm


admin.site.register(Article)
admin.site.register(ImageBlock)
admin.site.register(TextBlock)
admin.site.register(TinyMCEBlock, TinyMCEBlockAdmin)
