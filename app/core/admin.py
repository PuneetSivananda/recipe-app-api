from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {
            "fields": (
                'email',
                'password'
            ),
        }),
        (_('Personal info'), {"fields": ('name',)}),
        (_('Persmissions'), {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
        (_('Imporatnt Dates'), {"fields": ('last_login',)})
    )

    # add fields for user add filter
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
admin.site.register(models.Receipe)
