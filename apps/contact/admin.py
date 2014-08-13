from django.contrib import admin

from .models import Person, ModelChange


admin.site.register(Person)
admin.site.register(ModelChange)
