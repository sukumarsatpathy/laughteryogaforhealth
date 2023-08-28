from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import category, service


@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50"">'.format(object.image.url))
    thumbnail.short_description = 'Image'

    list_display = ('id', 'thumbnail', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = (
        (_('Category'), {'fields': ('title', 'slug', 'short_description', 'image', 'status')}),
    )


@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'category', 'title')
    search_fields = ('title',)
    fieldsets = (
        (_('Category'), {'fields': ('category', 'title', 'description', 'video_url')}),
        (_('Social Media'), {'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
        (_('Miscellaneous'), {'fields': ('status',)}),
    )