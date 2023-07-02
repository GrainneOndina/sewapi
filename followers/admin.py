from django.contrib import admin
from .models import Follow

class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('follower__username', 'followed__username')

admin.site.register(Follow, FollowAdmin)
