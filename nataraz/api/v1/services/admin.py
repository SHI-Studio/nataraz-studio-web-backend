from django.contrib import admin
from .models import Service, Tag

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Service, ServiceAdmin)
admin.site.register(Tag)
