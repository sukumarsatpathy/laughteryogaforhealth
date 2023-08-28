from django.contrib import admin
from django.utils.html import format_html
from .models import adBlock, lyJournals, banner, bannerImage, ContactPage, Copyright, webSettings, TermPages, pageCategory, AboutPage


@admin.register(adBlock)
class adBlockAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.image.url))
    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'title', 'type', 'status', 'submission_date')
    list_display_links = ('id', 'thumbnail', 'title')

    fieldsets = [
        ('adBlock Details', {'fields': ['type', 'title', 'image', 'url', 'status']}),
    ]


@admin.register(lyJournals)
class lyJournalsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.image.url))

    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'title', 'status', 'submission_date')
    list_display_links = ('id', 'thumbnail', 'title')

    fieldsets = [
        ('LY Journals Details', {'fields': ['title', 'image', 'status']}),
    ]


class bannerImageInline(admin.TabularInline):
    model = bannerImage
    extra = 1


@admin.register(banner)
class bannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'title')

    fieldsets = [
        ('Banner', {'fields': ['title', 'txt1', 'txt2', 'description', 'btn_txt', 'btn_url', 'status']}),
    ]

@admin.register(bannerImage)
class bannerImageAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.image.url))
    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'banner', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'banner')

    fieldsets = [
        ('Banner', {'fields': ['banner', 'image', 'status']}),
    ]


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'address', 'phone', 'email', 'modified_date', 'created_date')
    list_display_links = ('id', 'user', 'title')
    search_fields = ('title', 'address', 'phone', 'email')

    fieldsets = [
        ('Contact', {'fields': ['user', 'title', 'address', 'phone', 'email', 'map_url']}),
    ]


@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'modified_date', 'created_date')
    list_display_links = ('id', 'user', 'title')
    search_fields = ('title',)

    fieldsets = [
        ('Copyright', {'fields': ['user', 'symbol', 'startYear', 'title']}),
    ]


@admin.register(webSettings)
class webSettingsAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.logo.url))
    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'user', 'title', 'modified_date', 'created_date')
    list_display_links = ('id', 'user', 'title')

    fieldsets = [
        ('Frontend Settings', {'fields': ['user', 'title', 'slogan', 'logo', 'logo_white', 'logo_round']}),
        ('Social Media Setting', {'fields': ['fb_url', 'tw_url', 'ig_url', 'li_url']}),
        ('SEO Setting', {'fields': ['keywords', 'description']}),
    ]


@admin.register(TermPages)
class TermPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'updated_on')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = [
        ('Term Pages', {'fields': ['title', 'slug', 'description', 'status']}),
    ]


@admin.register(pageCategory)
class pageCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = [
        (('Page Category'), {'fields': ('title', 'slug', 'short_description', 'status')}),
    ]


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'modified_date', 'created_date')
    list_display_links = ('id', 'title')
    fieldsets = [
        ('About Pages Details', {'fields': ['category', 'title', 'description', 'status']}),
        ('SEO Details', {'fields': ['meta_title', 'meta_description', 'meta_keywords']}),
    ]