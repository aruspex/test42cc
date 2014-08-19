from django.views.generic import ListView

from .models import HttpRequestInfo
from apps.contact.models import Person


class RequestListView(ListView):
    model = HttpRequestInfo
    queryset = HttpRequestInfo.objects.all()[:10]
    context_object_name = 'requests'

    # Add person object tot template context
    def get_context_data(self, **kwargs):
        kwargs['person'] = Person.objects.all()[0]
        return super(RequestListView, self).get_context_data(**kwargs)
