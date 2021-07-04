from django.contrib import admin
from account.models import Account,publication,research_grant,patent,consultancy
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin','is_staff','PF_number','designation','mobile_number','department')
    search_fields = ('email','username',)
    readonly_fields =  ('date_joined','last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)
admin.site.register(publication)
admin.site.register(research_grant)
admin.site.register(patent)
admin.site.register(consultancy)

