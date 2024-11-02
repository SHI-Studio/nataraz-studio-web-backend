from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')

admin.site.register(Testimonial, TestimonialAdmin)
