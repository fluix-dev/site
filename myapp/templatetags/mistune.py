import mistune
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='mistune', is_safe=True)
@stringfilter
def mistune_html(text):
    return mistune.html(text)
