from django.contrib import admin
from .models import About, ExtraData

class AboutAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ExtraData)
admin.site.register(About, AboutAdmin)
