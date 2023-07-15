from django.contrib import admin
from .models import Follower

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'followed', 'created_at')  # Specify the fields to be displayed in the list view
    list_filter = ('created_at',)  # Specify the fields to be used for filtering
    search_fields = ('owner__username', 'followed__username')  # Specify the fields to be used for searching

admin.site.register(Follower, FollowerAdmin)
