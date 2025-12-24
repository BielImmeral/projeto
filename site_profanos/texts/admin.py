from django.contrib import admin
from .models import TextBlock

@admin.register(TextBlock)
class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('friend', 'order', 'is_locked')
    list_filter = ('friend', 'is_locked')
    ordering = ('friend', 'order')
