from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'post', 'created_at']  # Customize the displayed fields
    list_filter = ['created_at', 'post']  # Add filters for the created_at and post fields
    search_fields = ['content']  # Enable search for the content field
    readonly_fields = ['created_at', 'updated_at']  # Set certain fields as read-only
    date_hierarchy = 'created_at'  # Enable date-based hierarchy navigation
    ordering = ['-created_at']  # Set the default sorting order

    fieldsets = (
        ('Comment Details', {
            'fields': ('owner', 'post', 'parent_comment', 'content', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Make the timestamps collapsible
        }),
    )
