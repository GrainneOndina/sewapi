from rest_framework import generics, permissions
from sew_api.permissions import IsOwnerOrReadOnly
from .models import Follow
from .serializers import FollowSerializer

class FollowList(generics.ListCreateAPIView):
    """
    List all follows, i.e., all instances of a user following another user.
    Create a follow, i.e., follow a user if logged in.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class FollowDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follow.
    Destroy a follow, i.e., unfollow someone if the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
