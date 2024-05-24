from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from sewapi.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    API view for listing and creating comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def get_queryset(self):
        """
        Get the queryset for the comments list view.
        """
        parent_comment_id = self.kwargs.get('parent_comment_id')
        if parent_comment_id:
            queryset = Comment.objects.filter(parent_comment_id=parent_comment_id)
        else:
            queryset = Comment.objects.filter(parent_comment__isnull=True)
        return queryset

    def perform_create(self, serializer):
        """
        Perform creation of a new comment.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
