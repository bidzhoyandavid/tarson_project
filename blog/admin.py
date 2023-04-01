from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )
    search_fields = ()

admin.site.register(Blog, BlogAdmin)