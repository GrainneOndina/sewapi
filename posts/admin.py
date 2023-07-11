from .models import Post
from django.contrib import admin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'created_at']  # Customize the displayed fields
    list_filter = ['created_at']  # Add filters for the created_at field
    search_fields = ['content']  # Enable search for title and content

#from django.contrib import admin
#from .models import Post

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ['id', 'owner', 'created_at', 'updated_at', 'content', 'image', 'get_likes_count']
#    list_filter = ['created_at']
#    search_fields = ['content']

#    def get_likes_count(self, obj):
#        return obj.likes.count()


#    get_likes_count.short_description = 'Likes Count'
