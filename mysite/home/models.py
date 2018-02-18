from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validate_file_size


User = get_user_model()


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Request(models.Model):

    HOLIDAY = 'Holiday'
    SICK_LEAVE = 'Sick Leave'

    LEAVE_TYPE = (
        (HOLIDAY, 'Holiday'),
        (SICK_LEAVE, 'Sick Leave')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE, default=HOLIDAY)
    start = models.DateField()
    end = models.DateField()
    reason = models.TextField(max_length=200)
    status = models.CharField(max_length=10, default='Pending')
    attachment = models.FileField(upload_to=user_directory_path, null=True, validators=[validate_file_size])
    comment = models.TextField(max_length=200, blank=True, default="")

    def __str__(self):
        return '%s' % self.attachment

    def get_extension(self):
        return self.__str__().split('.').pop()


class RequesterManager(models.Manager):
    def get_authorisers(self):
        queryset = list(User.objects.filter(user_role='Authoriser').values_list('id', 'username'))

        return queryset


class Authoriser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.user


class Requester(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_authoriser = models.ForeignKey(Authoriser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s' % self.user


# creates a requester model object if created user's role is 'Requester'
@receiver(post_save, sender=User)
def create_requester(sender, instance, created, **kwargs):
    if created and instance.user_role == 'Requester':
        Requester.objects.create(user=instance)


# creates an authoriser model object if created user's role is 'Authoriser'
@receiver(post_save, sender=User)
def create_authoriser(sender, instance, created, **kwargs):
    if created and instance.user_role == 'Authoriser':
        Authoriser.objects.create(user=instance)


post_save.connect(create_authoriser, sender=User)
post_save.connect(create_requester, sender=User)
