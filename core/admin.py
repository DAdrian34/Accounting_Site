# core/admin.py

from django.contrib import admin
from django.utils.html import format_html

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email_clickable',
        'created_at',
        'is_handled',
        'reply_button',
    )
    list_filter = ('created_at', 'is_handled')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email')
        }),
        ('Mesaj', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_handled',)
        }),
        ('Info', {
            'fields': ('created_at',)
        }),
    )

    actions = ['mark_as_handled']

    def email_clickable(self, obj):
        return format_html(
            '<a href="mailto:{}">{}</a>',
            obj.email,
            obj.email
        )
    email_clickable.short_description = 'Email'

    def reply_button(self, obj):
        return format_html(
            '<a class="button" href="mailto:{}">Reply</a>',
            obj.email
        )
    reply_button.short_description = 'Quick Reply'

    def mark_as_handled(self, request, queryset):
        queryset.update(is_handled=True)
    mark_as_handled.short_description = 'Mark selected as handled'