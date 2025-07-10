from django.contrib import admin
from django.utils.html import format_html
from .models import Service  # Service is in this app
from .models import Project  # ✅ Correct if your app is named 'projects'


# Admin for Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail']

    def thumbnail(self, obj):
        if obj.image:  # Changed from 'icon' to 'image' to match model
            return format_html(
                '<img src="{}" width="60" height="40" style="object-fit: cover;" />',
                obj.image.url
            )
        return 'No Image'

    thumbnail.short_description = 'Preview'


# Admin for Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']
