from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from.models import UserProfile
@receiver(post_save,sender=User)
def create_user_profile(sender,instace,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance,email=instace.email,name=instance.username)
@receiver(post_save,sender=User)
def save_user_profile(sender,instace,**kwargs):
    instance.userprofile.save()