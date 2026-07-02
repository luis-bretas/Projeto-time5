from django.contrib import admin
from .models import Group, Activity


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'points_earned', 'duration_minutes', 'created_at')
    list_filter = ('group', 'created_at')
    search_fields = ('user__username', 'group__name', 'description')
