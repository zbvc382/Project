from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Requests(models.Model):

    HOLIDAY = 'Holiday'
    SICK_LEAVE = 'Sick Leave'

    LEAVE_TYPE = (
        (HOLIDAY, 'Holiday'),
        (SICK_LEAVE, 'Sick Leave')
    )

    user = models.CharField(max_length=20)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE, default=HOLIDAY)
    start = models.DateField()
    end = models.DateField()
    reason = models.TextField(max_length=200)
    status = models.CharField(max_length=10, default='pending')
    document = models.FileField(upload_to='media/', default='')
