from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='comments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Return a string representation of the comment.
        """
        return f'Comment {self.id}'
