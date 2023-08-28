from django.contrib import admin
from django.utils.html import format_html
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.image.url))
    thumbnail.short_description = 'Image'
    list_display = ('id', 'thumbnail', 'fullName', 'designation', 'status', 'submission_date')
    list_display_links = ('thumbnail', 'fullName')
    search_fields = ('fullName',)

    fieldsets = [
        ('Testimonial Details', {'fields': ['fullName', 'designation', 'message', 'image', 'status']}),
    ]
