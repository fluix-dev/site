import re

from .models import About, Blog, Project
from .templatetags.mistune import mistune_html_no_highlight

from django.contrib.syndication.views import Feed
from django.http import Http404
from django.utils import timezone
from django.utils.feedgenerator import Atom1Feed
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class MetadataMixin(object):
    title = "TheAvidDev"
    description = "Somwhere on the internet..."
    og_type = "website"

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_og_type(self):
        return self.og_type

    def get_context_data(self, **kwargs):
        return {
            "title": self.get_title(),
            "description": self.get_description(),
            "og_type": self.get_og_type(),
            **super().get_context_data(**kwargs)
        }



class IndexView(MetadataMixin, ListView):
    model = Blog
    template_name = "index.html"
    context_object_name = "blogs"
    title = "TheAvidDev's Blog"

    def get_description(self):
        return About.objects.get().description

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            return qs.filter(published_at__lte=timezone.now())
        return qs


class TimelineView(IndexView):
    template_name = "timeline.html"
    title = "Blog Timeline"
    description = "A timeline of all the blogs I've ever written."


class RSSBlogFeed(Feed):
    title = "TheAvidDev's Blog"
    link = "/"
    description = "Somewhere on the internet..."

    def items(self):
        return Blog.objects.filter(published_at__lte=timezone.now())[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return mistune_html_no_highlight(item.content)


class AtomBlogFeed(RSSBlogFeed):
    feed_type = Atom1Feed
    subtitle = RSSBlogFeed.description


class BlogView(MetadataMixin, DetailView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"
    og_title = "article"

    def get_title(self):
        return self.get_object().title.split("-")[0]

    def get_description(self):
        # Remove newlines and markup links
        regex = "[\\[\\]\\n\\r]|\\([^\\(\\)]+\\)"
        content = self.get_object().content.split("<!--break-->")[0]
        return re.sub(regex, "", content)

    def get_object(self):
        blog = super().get_object()
        if not self.request.user.is_staff and blog.hidden:
            raise Http404()
        return blog


class ProjectsView(MetadataMixin, ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"
    title = "Project List"

    def get_description(self):
        return ("A list of the most notable projects I've worked on "
            "throughout the years. It ranges from websites, to applications, to "
            "tools, and random scripts.")


class AboutView(MetadataMixin, TemplateView):
    template_name = "about.html"
    title = "About Page"

    def get_description(self):
        return About.objects.get().description
