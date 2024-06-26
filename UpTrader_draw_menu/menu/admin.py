from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'named_url', 'parent')
    list_filter = ('parent',)
    search_fields = ('title', 'parent')


admin.site.register(MenuItem, MenuItemAdmin)
