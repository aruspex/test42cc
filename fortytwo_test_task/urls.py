from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.hello.views.hello', name='hello'),
    url(r'^admin/', include(admin.site.urls)),
)
