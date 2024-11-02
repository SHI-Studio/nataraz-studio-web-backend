from django.contrib import admin
from .models import Blog, Category, Paragraph

class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cover')
    search_fields = ('title', 'author')
    inlines = [ParagraphInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
