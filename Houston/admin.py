from django.contrib import admin

from .models import *

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    ordering = ('-report_time',)
    list_display = ('user', 'path', 'report_time', 'session')
