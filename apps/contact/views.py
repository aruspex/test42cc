from django.shortcuts import render

from .forms import PersonForm
from .models import Person


def contacts(request):
    person = Person.objects.all()[0]
    return render(request,
                  'contact/contacts.html',
                  {'person': person}
           )


def form(request):
    form = PersonForm()
    return render(request, 'contact/form.html', {'form': form})
