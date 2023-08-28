from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from  embed_video.admin  import  AdminVideoMixin
from .models import imgCategory, imgGallery, vdoCategory, vdoGallery


class imgGalleryinline(admin.TabularInline):
    model = imgGallery
    extra = 1


@admin.register(imgCategory)
class imgCategoryAdmin(admin.ModelAdmin):
    inlines = [
        imgGalleryinline
    ]
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50"">'.format(object.image.url))
    thumbnail.short_description = 'Image'

    list_display = ('id', 'thumbnail', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = (
        (_('Gallery'), {'fields': ('title', 'slug', 'image', 'status')}),
    )


class vdoGalleryinline(admin.TabularInline):
    model = vdoGallery
    extra = 1


@admin.register(vdoCategory)
class vdoCategoryAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
    inlines = [
        vdoGalleryinline
    ]

    def thumbnail(self, object):
        return format_html('<img src="{}" width="50"">'.format(object.image.url))
    thumbnail.short_description = 'Image'

    list_display = ('id', 'thumbnail', 'title', 'modified_date', 'created_date')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = (
        (_('Video Category'), {'fields': ('title', 'slug', 'image')}),
    )