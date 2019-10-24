from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, help_text='The time this model was created at.')
    updated_at = models.DateTimeField(auto_now=True, help_text='The last time this model was modified at.')

    class Meta:
        abstract = True

class ContactMessage(TimeStampMixin):
    name = models.CharField(max_length=100, editable=False, help_text='The name provided by the user.')
    email = models.EmailField(editable=False, help_text='The email provided by the user.')
    message = models.TextField(max_length=2047, editable=False, help_text='The message provided by the user.')

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField(help_text='An image representing the project')
    name = models.CharField(max_length=100, help_text='The name or title of the project.')
    description = models.TextField(max_length=2047, help_text='A description of the project.')
    local_link = models.URLField(blank=True, help_text='Link to the running project.')
    source_link = models.URLField(blank=True, help_text="Link to the project's source code.")
    sort_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['sort_order']

    def __str__(self):
        return self.name

    def get_description(self):
        return mark_safe(self.description)
