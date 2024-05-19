from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'is_active',)
    list_filter = ('is_active', 'position',)
    search_fields = ('first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name',)
