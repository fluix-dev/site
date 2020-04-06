import logging

from .forms import ContactForm
from .models import Blog, ContactMessage, Project

from django.shortcuts import get_object_or_404, render, reverse
from django.http import HttpResponse
from django.utils import timezone

logger = logging.getLogger(__name__)


def index(request):
    context = {
        "blogs": Blog.objects.all()
        .filter(published_at__lte=timezone.now())
        .order_by("published_at")
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug, published_at__lte=timezone.now())
    return render(request, "blog.html", {"blog": blog})


def contact(request):
    if request.method == "POST":
        cf = ContactForm(request.POST)

        # Set default fail message
        message = "Failed... Try again later."
        if cf.is_valid():
            # Create message object
            cm = ContactMessage()
            cm.name = cf.cleaned_data["name"]
            cm.email = cf.cleaned_data["email"]
            cm.message = cf.cleaned_data["message"]
            cm.save()

            # Log message
            logger.info(
                "New contact message: %s",
                request.build_absolute_uri(
                    reverse("admin:myapp_contactmessage_change", args=(cm.id,))
                ),
            )

            # Success Message
            message = "Sent!"
        return HttpResponse(message)

    context = {
        "form": ContactForm(),
    }
    return render(request, "contact.html", context)


def projects(request):
    context = {
        "projects": Project.objects.all().order_by("sort_order"),
    }
    return render(request, "projects.html", context)
