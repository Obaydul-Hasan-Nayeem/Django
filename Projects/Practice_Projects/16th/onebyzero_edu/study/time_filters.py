from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def humanize_time(timestamp):
    return timesince(timestamp)
