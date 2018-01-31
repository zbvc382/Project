from django.contrib import admin
from .models import Request, Requester


class RequesterAdmin(admin.ModelAdmin):
    model = Requester
    list_display = ['get_username', 'get_email_address', 'get_is_active',
                    'assigned_authoriser']

    def get_username(self, obj):
        return obj.user.username

    def get_email_address(self, obj):
        return obj.user.email

    def get_is_active(self, obj):
        return obj.user.is_active

    get_username.admin_order_field = 'user'
    get_username.short_description = 'USERNAME'
    get_email_address.short_description = 'EMAIL ADDRESS'
    get_is_active.short_description = 'IS ACTIVE'
    search_fields = ('user__username',)


admin.site.register(Request)
admin.site.register(Requester, RequesterAdmin)