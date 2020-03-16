from .models import ContactMessage, Project

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    # Displayed in list view
    date_hierarchy = 'updated_at'
    list_display = ('name', 'email', 'message_truncate', 'created_at')

    def message_truncate(self, obj):
        return obj.message[:80]

    # Displayed in model editing
    readonly_fields = ('name', 'email', 'message', 'created_at', 'updated_at')
    fieldsets = (
        ('Message', {
            'fields': ('name', 'email', 'message')
        }),
        ('Dates and Times', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

admin.site.site_header = 'Site Administration'

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Project, ProjectAdmin)
