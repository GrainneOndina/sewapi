from django.contrib.auth.models import User
from django.db import models
from posts.models import Post


class Like(models.Model):
    """
    Model representing a like on a post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, related_name='post_likes', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        """
        Returns a string representation of the like.
        Format: owner post
        """
        return f'{self.owner} {self.post}'
