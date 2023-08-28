from django.contrib import admin
from .models import Contact, Invite, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'email', 'submitted_date')
    list_display_links = ('id', 'fullName', 'email')
    search_fields = ('fullName',)
    fieldsets = [
        ('Contact Details', {'fields': ['fullName', 'email', 'message']}),
    ]


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullName', 'email', 'contact', 'country', 'submitted_date')
    list_display_links = ('id', 'fullName', 'email')
    search_fields = ('fullName',)
    fieldsets = [
        ('Invite Details', {'fields': ['fullName', 'email', 'contact', 'country', 'message']}),
    ]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'status', 'submitted_date')
    list_display_links = ('id', 'email')
    search_fields = ('email',)
    fieldsets = [
        ('Subscriber Details', {'fields': ['email', 'status']}),
    ]