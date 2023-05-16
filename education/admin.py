from django.contrib import admin
from .models import *

# Register your models here.


class VocabularyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_upload")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = (
        "id",
        "title",
    )


class EducationPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_upload")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = (
        "id",
        "title",
    )


admin.site.register(Vocabulary, VocabularyAdmin)
admin.site.register(EducationPost, EducationPostAdmin)
