import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import PersonForm
from .models import Person


def contacts(request):
    person = Person.objects.all()[0]
    return render(request,
                  'contact/contacts.html',
                  {'person': person})


@login_required
def edit_form(request):
    """
    Handles person form edition

    If form is not valid and request.is_ajax - return json
    dictionary that contains all errors. If request is not ajax (initial GET) -
    simply render form with data from Person model.
    """
    instance = Person.objects.all()[0]
    form = PersonForm(
        request.POST or None,
        request.FILES or None,
        instance=instance
    )
    if form.is_valid():
        form.save()
        return redirect('contacts')
    elif request.is_ajax():
        errors = {'errors': dict(form.errors.items())}
        return HttpResponse(json.dumps(errors), mimetype='application/json')
    else:
        return render(request, 'contact/edit_person_form.html', {'form': form})
