import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^faction/', include('faction.urls')),
    (r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )