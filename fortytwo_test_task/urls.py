from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.http_storage_middleware.views import RequestListView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'apps.contact.views.contacts', name='contacts'),
    url(r'^requests/$', RequestListView.as_view(), name='requests'),
    url(r'^form/$', 'apps.contact.views.edit_form', name='edit_form'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += staticfiles_urlpatterns()
