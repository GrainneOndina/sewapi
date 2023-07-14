from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from django.contrib.contenttypes.models import ContentType

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    image = serializers.ImageField(required=False)
    url = serializers.URLField(required=False)
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_like_id(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                like = Like.objects.get(user=request.user, content_type=ContentType.objects.get_for_model(Post), object_id=obj.id)
                return like.id
            except Like.DoesNotExist:
                return None
        return None

    
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'content', 'image', 'url', 'like_id', 'likes_count'
        ]