from django.contrib import admin
from .models import *


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "date_created",
    )
    list_display_links = ("id", "title")
    search_fields = ("title",)


admin.site.register(Blog, BlogAdmin)
