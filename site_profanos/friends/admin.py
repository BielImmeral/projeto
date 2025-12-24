from django.contrib import admin
from .models import Friend

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
