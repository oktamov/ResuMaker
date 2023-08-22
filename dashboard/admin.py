from django.contrib import admin

from dashboard.models import Resume, Skills


@admin.register(Resume)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Skills)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
