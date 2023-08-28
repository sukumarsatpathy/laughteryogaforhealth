from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import Account, UserProfile


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()

    fieldsets = [
        ('Login Details', {'fields': ['email', 'username', 'password']}),
        ('User Details', {'fields': ['first_name', 'last_name']}),
        ('Permission Details', {'fields': ['is_admin', 'is_staff', 'is_active', 'is_superadmin']}),
    ]


admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)


class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'modified_date', 'created_date')
    list_display_links = ('thumbnail', 'user')

    fieldsets = [
        ('User Details', {'fields': ['user', 'picture', 'designation', 'company_name', 'phone_number', 'address_line_1', 'address_line_2']}),
    ]


admin.site.register(UserProfile, UserProfileAdmin)