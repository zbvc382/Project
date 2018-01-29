from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
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

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_requested = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE, default=HOLIDAY)
    start = models.DateField()
    end = models.DateField()
    reason = models.TextField(max_length=200)
    status = models.CharField(max_length=10, default='pending')
    attachment = models.FileField(upload_to=user_directory_path, blank=True, null=True)
