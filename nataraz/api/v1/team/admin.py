from django.contrib import admin
from .models import Member, ExtraData

class MemberAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')

class ExtraDataAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Member, MemberAdmin)
admin.site.register(ExtraData, ExtraDataAdmin)
