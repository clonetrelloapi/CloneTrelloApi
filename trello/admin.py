from django.contrib import admin
from .models import *

class TitleOption(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Title, TitleOption)

class CardOption(admin.ModelAdmin):
    list_display = ['id', 'title', 'cardTitle','create_date', 'update_date']

admin.site.register(Card, CardOption)

class CommentOption(admin.ModelAdmin):
    list_display = ['id', 'card', 'comment']

admin.site.register(Comments, CommentOption)