from django.contrib import admin
from .models import Places, Categories, Sales


# Register your models here.


class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creates_at', 'category', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Places, PlacesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sales, SalesAdmin)
