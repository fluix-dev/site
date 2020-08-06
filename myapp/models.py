from .templatetags.mistune import mistune_html

from django.db import models
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.safestring import mark_safe
from solo.models import SingletonModel


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="The time this model was created at."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The last time this model was modified at."
    )

    class Meta:
        abstract = True


class About(SingletonModel):
    description = models.TextField(help_text="Description placed beside image.")
    content = models.TextField(help_text="Content below description and image.")


class Blog(TimeStampMixin):
    slug = models.SlugField(primary_key=True, help_text="Slug for blog.")
    title = models.CharField(max_length=255, help_text="Blog title.")
    tag = models.CharField(max_length=50, help_text="Blog tag.")
    published_at = models.DateTimeField(
        help_text="Date this blog was published on."
    )
    content = models.TextField(
        max_length=35565, help_text="Markdown and/or HTML blog content."
    )

    def __str__(self):
        return self.title

    def get_time_length(self):
        return int(len(self.content.split()) / 125)

    def get_absolute_url(self):
        return reverse("blog", args=[self.slug])

    def get_admin_url(self):
        return reverse("admin:myapp_blog_change", args=[self.slug])

    @property
    def hidden(self):
        return self.published_at > timezone.now()

    @property
    def snippet(self):
        html = mistune_html(self.content).split("<!--break-->")
        if len(html) == 1:
            return mark_safe(truncatewords_html(html[0], 150))
        return mark_safe(html[0])

    class Meta:
        ordering = ["-published_at"]


class Project(models.Model):
    image = models.ImageField(help_text="An image representing the project")
    name = models.CharField(
        max_length=100, help_text="The name or title of the project."
    )
    description = models.TextField(
        max_length=2047, help_text="A description of the project."
    )
    local_link = models.URLField(
        blank=True, help_text="Link to the running project."
    )
    source_link = models.URLField(
        blank=True, help_text="Link to the project's source code."
    )
    writeup_link = models.URLField(
        blank=True, help_text="Link to writeup or blog about project."
    )
    sort_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ["sort_order"]

    def __str__(self):
        return self.name

    def get_description(self):
        return mark_safe(self.description)
