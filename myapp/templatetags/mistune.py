import mistune
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='mistune', is_safe=True)
def mistune_html(text):
    return mark_safe(mistune.html(text))
