from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView
from frontend.models import Response, Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(r'^blogonymous/', include('frontend.urls')),                   
    url(r'^yeah/', 'yeah'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
