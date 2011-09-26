from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView
from frontend.models import Response, Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    (r'^$', 'home'),
    (r'^(?P<entry_id>\d+)/$', 'detail'),
    (r'^answer/', CreateView.as_view(model=Response, success_url="/frontend/")),
    (r'^submit/(?P<entry_id>\d+)/$', 'submit'),
    (r'^submit/(?P<entry_id>\d+)/enter/', 'enter'),
    (r'^single/(?P<entry_id>\d+)/$', 'single'),
    (r'^question/$', 'question'),
    (r'^question/enter/$', 'question_submit'),
    (r'^about', 'about'),
    (r'^single/(?P<entry_id>\d+)/upvote/', 'upvote'),                   
)
