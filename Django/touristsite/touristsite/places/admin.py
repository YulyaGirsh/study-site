from django.contrib import admin
from .models import Places


# Register your models here.


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'creates_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Places, PlacesAdmin)
