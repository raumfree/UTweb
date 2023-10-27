from django.contrib import admin

from .models import *


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item', 'cat')
    search_fields = ('cat',)
    prepopulated_fields = {"slug": ('item',)}


admin.site.register(Categories)
admin.site.register(Items, ItemsAdmin)
