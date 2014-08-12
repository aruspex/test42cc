from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper


class SignupUserForm(forms.ModelForm):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4, widget=PasswordInput)
    verify_password = forms.CharField(min_length=4, widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(SignupUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    def clean(self):
        cleaned_data = super(SignupUserForm, self).clean()
        password = cleaned_data.get('password')
        verify_password = cleaned_data.get('verify_password')
        if password != verify_password:
            raise forms.ValidationError('Passwords do not match')
        else:
            return cleaned_data
