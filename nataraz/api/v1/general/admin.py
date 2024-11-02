from django.contrib import admin
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_text', 'file')

admin.site.register(Media, MediaAdmin)
