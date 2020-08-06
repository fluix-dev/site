from django.views.generic.base import TemplateView


class RobotView(TemplateView):
    template_name = "robots.txt"
    content_type = "text/plain"
