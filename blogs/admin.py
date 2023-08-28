from django.contrib import admin
from django.utils.html import format_html
from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="100">'.format(object.image.url))
    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'title', 'status', 'views', 'submission_date')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = [
        ('Blog Details', {'fields': ['title', 'slug', 'description', 'image', 'views', 'status']}),
        ('SEO Details', {'fields': ['meta_title', 'meta_description', 'meta_keywords']}),
    ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'blog', 'fullName', 'email', 'status', 'submission_date')
#     list_display_links = ('blog', 'fullName')
#     search_fields = ('blog__title', 'fullName')
#
#     fieldsets = [
#         ('Comment Details', {'fields': ['blog', 'fullName', 'email', 'message', 'ip', 'status']}),
#     ]