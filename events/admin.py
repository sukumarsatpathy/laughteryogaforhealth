from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'organiser', 'start_date', 'end_date', 'modified_date', 'created_date', 'views')
    list_display_links = ('id', 'title', 'organiser')
    search_fields = ('title', 'organiser')
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = [
        ('Event Basic Details', {'fields': ['title', 'slug', 'description', 'start_date', 'end_date', 'location']}),
        ('Organizer Details', {'fields': ['organiser', 'email', 'contact_no']}),
        ('Images and Videos', {'fields': ['image', 'video']}),
        ('Miscellaneous', {'fields': ['status', ]}),
        ('SEO Details', {'fields': ['meta_title', 'meta_description', 'meta_keywords' ]}),
    ]