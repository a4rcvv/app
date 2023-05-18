from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at', 'id', 'body', 'user')
    list_filter = ('created_at', 'updated_at', 'user')
    date_hierarchy = 'created_at'
