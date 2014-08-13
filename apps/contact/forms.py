from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Submit, Div, Field, ButtonHolder, Button
)

from .models import Person
from .widgets import CalendarWidget


class PersonForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput)
    birth_date = forms.DateField(widget=CalendarWidget)

    class Meta:
        model = Person

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(Div('name',
                    'surname',
                    'birth_date',
                    'photo',
                    Div(template="crispy/photo_placeholder.html"),
                    css_class="span5"),
                Div('email',
                    'jabber',
                    'skype',
                    Field('other_contacts',
                          css_class='man_left',
                          template='crispy/custom_field.html'),
                    Field('bio',
                          css_class="man_left",
                          wrapper_class="fuu",
                          template='crispy/custom_field.html'),
                    css_class='span5'),
                css_class='row')
        )
