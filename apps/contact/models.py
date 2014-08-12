from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25)
    birth_date = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()

    def __unicode__(self):
        return "{} {}".format(self.name, self.surname)
