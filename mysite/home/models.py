from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Requests(models.Model):

    HOLIDAY = 'HO'
    SICK_LEAVE = 'SL'

    LEAVE_TYPE = (
        (HOLIDAY, 'Holiday'),
        (SICK_LEAVE, 'Sick Leave')
    )

    user = models.CharField(max_length=20, default='')
    leave_type = models.CharField(max_length=2, choices=LEAVE_TYPE, default=HOLIDAY)
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=10, default='pending')
