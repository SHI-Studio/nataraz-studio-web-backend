from django.contrib import admin
from .models import Work, Contributor, ExtraData, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ExtraDataInline(admin.StackedInline):
    model = ExtraData
    extra = 1 

class WorkAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ExtraDataInline]
    list_display = ('title', 'date')

admin.site.register(Work, WorkAdmin)
admin.site.register(Contributor)
