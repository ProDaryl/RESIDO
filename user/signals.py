from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.dispatch import receiver
User = get_user_model()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)