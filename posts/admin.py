from .models import Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'created_at']  # Customize the displayed fields
    list_filter = ['created_at']  # Add filters for the created_at field
    search_fields = ['content']  # Enable search for title and content
