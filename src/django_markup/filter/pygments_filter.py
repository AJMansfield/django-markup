from django.template.defaultfilters import linebreaks
from django_markup.filter import MarkupFilter

class LinebreaksMarkupFilter(MarkupFilter):
    """
    Uses Pygments to highlight <code> parts of a text. This filter is supposed
    to be used after another filter that produces <code> blocks, such as
    Markdown or RestructuredText. Example:

        text = "Some Javascript: <code>alert('foo');</code>"
        text = formatter(text, filter_name='markdown')
        text = formatter(text, filter_name='pygments')
        print text
    """
    title = 'Pygments'

    def render(self, text, **kwargs):
        return linebreaks(text, **kwargs)
