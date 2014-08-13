from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse

from ..models import Person


register = template.Library()


@register.assignment_tag
def photo_preview():
    return Person.objects.all()[0].photo.url


@register.simple_tag
def edit_link(object):
    """
    Accepts any object and renders the link to its admin edit page
    """
    ct = ContentType.objects.get_for_model(object)
    url = reverse(
        'admin:{}_{}_change'.format(ct.app_label, ct.model),
        args=[object.pk]
    )
    return url