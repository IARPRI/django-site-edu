from django.contrib import admin

from .models import *


class AIAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(AI, AIAdmin)
admin.site.register(Category, CategoryAdmin)