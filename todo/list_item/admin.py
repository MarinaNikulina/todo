from django.contrib import admin
from list_item.models import ListItemModel


class ListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'list_model']
    list_filter = ['created', 'name', 'is_done', 'list_model']
    search_fields = ['name', 'list_model__name']


admin.site.register(ListItemModel, ListItemAdmin)

