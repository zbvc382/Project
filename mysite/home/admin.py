from django.contrib import admin
from .models import Request, Requester

# Register your models here.

admin.site.register(Request)
admin.site.register(Requester)