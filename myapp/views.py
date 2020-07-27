from .models import Blog, Project
from .templatetags.mistune import mistune_html_no_highlight

from django.contrib.syndication.views import Feed
from django.http import Http404
from django.utils import timezone
from django.utils.feedgenerator import Atom1Feed
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class IndexView(ListView):
    model = Blog
    template_name = "index.html"
    context_object_name = "blogs"

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            return qs.filter(published_at__lte=timezone.now())
        return qs


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


class BlogView(DetailView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"

    def get_object(self):
        blog = super().get_object()
        if not self.request.user.is_staff and blog.hidden:
            raise Http404()
        return blog


class ProjectsView(ListView):
    model = Project
    template_name = "projects.html"
    context_object_name = "projects"


class AboutView(TemplateView):
    template_name = "about.html"
