from django.contrib import admin
from .models import Films, Category


class FilmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_start_view', 'date_end_view', 'running_time', 'age', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'date_start_view', 'date_end_view')
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Films, FilmsAdmin)
admin.site.register(Category, CategoryAdmin)
