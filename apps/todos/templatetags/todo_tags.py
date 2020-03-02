from django import template

from apps.todos.models import Topic


register = template.Library()

@register.filter
def bg_color(topic):
    colors = [
        'badge-primary', 'badge-success', 'badge-danger', 'badge-warning',
        'badge-info', 'badge-dark'
    ]
    index = topic.id % len(colors)

    return colors[index]



