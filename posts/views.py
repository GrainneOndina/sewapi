from django.db.models import Count
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from sewapi.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        """
        Saves the post with the requesting user as the owner.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')
