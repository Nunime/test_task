from django.contrib import admin
from .models import Menu, MenuItem

class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 1
    fk_name = 'parent'

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu', 'parent', 'order')
    list_filter = ('menu',)
    ordering = ('menu', 'parent__id', 'order')
