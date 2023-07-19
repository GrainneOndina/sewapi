from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validate the image field.
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the comment.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, instance):
        """
        Return the humanized created_at timestamp.
        """
        return naturaltime(instance.created_at)

    def get_updated_at(self, obj):
        """
        Return the humanized updated_at timestamp.
        """
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'parent_comment',
            'content', 'image', 'created_at', 'updated_at',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model that includes replies.
    """
    replies = serializers.SerializerMethodField()

    def get_replies(self, obj):
        """
        Return the serialized replies for the comment.
        """
        replies = Comment.objects.filter(parent_comment=obj)
        serializer = CommentSerializer(replies, many=True, context=self.context)
        return serializer.data

    class Meta(CommentSerializer.Meta):
        fields = CommentSerializer.Meta.fields + ['replies']
