from .models import Blog, Project

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin


class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_at'
    list_display = (
        'title',
        'tag',
        'content_truncate',
        'published_at',
        'created_at',
        'updated_at',
    )

    def content_truncate(self, obj):
        return obj.content[:80]

    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Details', {'fields': ('slug', 'title', 'tag', 'published_at')}),
        ('Content', {'fields': ('content',)}),
        ('Dates', {'fields': ('created_at', 'updated_at')}),
    )


class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


admin.site.site_header = 'Site Administration'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
