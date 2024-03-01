from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']  # Specify fields you want to search on

admin.site.register(Blog, BlogAdmin)