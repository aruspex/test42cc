from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25, verbose_name=u'Last name')
    birth_date = models.DateField(verbose_name=u'Date of birth')
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=30)
    other_contacts = models.TextField()
    photo = models.ImageField(upload_to="contact_photo", null=True, blank=True)

    def __unicode__(self):
        return "{} {}".format(self.name, self.surname)
