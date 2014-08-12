from django.shortcuts import render

from .models import Person


def contacts(request):
    person = Person.objects.all()[0]
    return render(request,
                  'contact/contacts.html',
                  {'person': person}
           )
