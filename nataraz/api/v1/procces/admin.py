from django.contrib import admin
from .models import Process

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('step', 'title', 'subtitle')
    ordering = ('step',)

admin.site.register(Process, ProcessAdmin)
