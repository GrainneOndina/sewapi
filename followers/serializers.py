from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    followed = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follow
        fields = [
            'id', 'owner', 'created_at', 'followed', 
        ]
