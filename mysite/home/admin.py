from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Request, Requester, Authoriser

User = get_user_model()


class RequesterAdmin(admin.ModelAdmin):
    model = Requester
    list_display = ['get_username', 'get_assigned_to', 'get_email_address',
                    'get_is_active']

    def get_username(self, obj):
        return obj.user.username

    def get_email_address(self, obj):
        return obj.user.email

    def get_is_active(self, obj):
        return obj.user.is_active

    def get_assigned_to(self, obj):
        try:
            return obj.assigned_authoriser.user.username

        except AttributeError:
            return None

    # Changes the representation of user in the user selection list
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        field = super(RequesterAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "user":
            field.label_from_instance = lambda u: "%s" % u.username
        if db_field.name == "assigned_authoriser":
            field.label_from_instance = lambda u: "%s" % u.user.username
        return field

    if get_assigned_to is not None:
        get_assigned_to.short_description = 'ASSIGNED TO'

    get_username.short_description = 'USERNAME'
    get_email_address.short_description = 'EMAIL ADDRESS'
    get_is_active.short_description = 'IS ACTIVE'
    search_fields = ('user__username',)


class AuthoriserAdmin(admin.ModelAdmin):
    model = Requester
    list_display = ['get_username', 'get_email_address', 'get_is_active',]

    def get_username(self, obj):
        return obj.user.username

    def get_email_address(self, obj):
        return obj.user.email

    def get_is_active(self, obj):
        return obj.user.is_active

    get_username.short_description = 'USERNAME'
    get_email_address.short_description = 'EMAIL ADDRESS'
    get_is_active.short_description = 'IS ACTIVE'
    search_fields = ('user__username',)


admin.site.register(Authoriser, AuthoriserAdmin)
admin.site.register(Request)
admin.site.register(Requester, RequesterAdmin)
