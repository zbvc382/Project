from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    phone_number = models.IntegerField(default=0)
    department = models.CharField(max_length=100, default='')

    def __str__(self):
        return '%s' % self.user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
