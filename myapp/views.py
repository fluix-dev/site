from .models import Blog, Project

from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse
from django.utils import timezone


def index(request):
    if request.user.is_staff:
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.all().filter(published_at__lte=timezone.now())
    context = {"blogs": blogs.order_by("-published_at")}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def blog(request, slug):
    if request.user.is_staff:
        blog = get_object_or_404(Blog, slug=slug)
    else:
        blog = get_object_or_404(
            Blog, slug=slug, published_at__lte=timezone.now()
        )
    return render(request, "blog.html", {"blog": blog})


def projects(request):
    context = {
        "projects": Project.objects.all().order_by("sort_order"),
    }
    return render(request, "projects.html", context)
