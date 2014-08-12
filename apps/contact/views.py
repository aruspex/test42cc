from django.contrib.auth.decorators import login_required
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
    instance = Person.objects.all()[0]
    form = PersonForm(
        request.POST or None,
        request.FILES or None,
        instance=instance
    )
    if form.is_valid():
        form.save()
        return redirect('contacts')
    else:
        return render(request, 'contact/edit_person_form.html', {'form': form})
