import mistune
from django import template
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"


@register.filter(name="mistune", is_safe=True)
def mistune_html(text):
    markdown = mistune.create_markdown(renderer=HighlightRenderer())
    return mark_safe(markdown(text))
