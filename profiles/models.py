from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='../syjunta_vvcd8h')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        Returns a string representation of the profile.
        """
        return f"{self.owner}"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to create a profile when a new user is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
