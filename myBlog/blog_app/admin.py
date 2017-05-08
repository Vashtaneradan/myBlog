from django.db import models
from django.contrib import admin

from .models import Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ('publish_date', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)

