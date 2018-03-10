from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Request, Requester, Authoriser, Template, Restriction

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


class RestrictionAdmin(admin.ModelAdmin):
    model = Restriction
    list_display = ['get_number', 'get_username', 'from_date', 'to_date']

    def get_username(self, obj):
        return obj.user.user.username

    def get_number(self, obj):
        return obj.id

    get_username.short_description = 'USERNAME'
    get_number.short_description = '#'


class TemplateAdmin(admin.ModelAdmin):
    model = Template
    list_display = ['get_number', 'get_username', 'get_template_name', 'get_created_at']

    def get_username(self, obj):
        return obj.user.username

    def get_number(self, obj):
        return obj.id

    def get_template_name(self, obj):
        return obj.template_name

    def get_created_at(self, obj):
        return obj.created_at

    get_username.short_description = 'USERNAME'
    get_number.short_description = '#'
    get_template_name.short_description = 'TEMPLATE NAME'
    get_created_at.short_description = 'CREATE DATE'


class RequestAdmin(admin.ModelAdmin):
    model = Template
    list_display = ['get_username', 'get_leave_type', 'get_start_date', 'get_end_date',
                    'get_created_at']

    def get_username(self, obj):
        return obj.user.username

    def get_leave_type(self, obj):
        return obj.leave_type

    def get_start_date(self, obj):
        return obj.start

    def get_end_date(self, obj):
        return obj.end

    def get_created_at(self, obj):
        return obj.created_at

    get_username.short_description = 'USERNAME'
    get_leave_type.short_description = 'LEAVE TYPE'
    get_start_date.short_description = 'START DATE'
    get_end_date.short_description = 'END DATE'
    get_created_at.short_description = 'CREATE DATE'


admin.site.register(Request, RequestAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Restriction, RestrictionAdmin)
admin.site.register(Authoriser, AuthoriserAdmin)
admin.site.register(Requester, RequesterAdmin)
