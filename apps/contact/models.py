from django.db import models, DatabaseError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


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
        return "{0} {1}".format(self.name, self.surname)


class ModelChange(models.Model):
    TYPE_CHOICES = (
        ('C', 'Created'),
        ('U', 'Updated'),
        ('D', 'Deleted')
    )
    model_name = models.CharField(max_length=100)
    change_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s %s" % (self.change_type, self.model_name)


@receiver(post_save)
def do_on_save(sender, **kwargs):
    model_name = kwargs['instance']._meta.object_name
    if model_name == 'ModelChange':
        return
    if kwargs['created']:
        change_type = 'C'
    else:
        change_type = 'U'
    try:
        ModelChange.objects.create(
            model_name=model_name, change_type=change_type)
    except DatabaseError:
        pass


@receiver(post_delete)
def do_on_delete(sender, **kwargs):
    model_name = kwargs['instance']._meta.object_name
    if model_name == 'ModelChange':
        return
    try:
        ModelChange.objects.create(model_name=model_name, change_type='D')
    except DatabaseError:
        pass
