from django import template

from ..models import Person


register = template.Library()


@register.assignment_tag
def photo_preview():
    return Person.objects.all()[0].photo.url
