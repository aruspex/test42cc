from django.db import models


class HttpRequestInfo(models.Model):
    """
    Stores information about requests collected by middleware.
    """
    date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=150)
    is_ajax = models.BooleanField()

    def __unicode__(self):
        return '{} {}'.format(self.method, self.path)
