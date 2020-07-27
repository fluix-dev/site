from .models import Blog, Project

from django.http import Http404
from django.utils import timezone
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
