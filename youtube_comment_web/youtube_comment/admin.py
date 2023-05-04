from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(WordCloud)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Keyword)
admin.site.register(Trending)