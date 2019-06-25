from django.contrib import admin
from .models import *

class ListOption(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(List, ListOption)

class CardOption(admin.ModelAdmin):
    list_display = ['id', 'list', 'title', 'create_date', 'update_date']

admin.site.register(Card, CardOption)