from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _

from rest_framework.reverse import reverse

from apps.user.models import CustomUser, UserQueue


class CustomUserAdmin(UserAdmin):
    """Кастомная админка для пользователя"""

    list_display = ('username', 'email', 'is_staff', 'chat_id')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'email', 'chat_id')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(UserQueue)
class UserQueueModel(admin.ModelAdmin):
    """Админка для очереди пользователей"""

    def button_add_user(self, obj):
        """Кнопки добавить пользователя"""

        return mark_safe(f'<a href="{reverse("add_user_from_queue", args=(obj.chat_id,))}">add</a>')

    list_display = ('id', 'chat_id', 'username', 'first_name', 'last_name', 'button_add_user')
