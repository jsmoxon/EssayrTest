from django.conf.urls.defaults import patterns, include, url
from django.views.generic import CreateView
from frontend.models import Response, Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'question_of_day'),
    (r'^questions', 'home'),
    (r'^pk', 'pk'),
    (r'^answer/', CreateView.as_view(model=Response, success_url="/frontend/")),
    (r'^submit/(?P<entry_id>\d+)/$', 'submit'),
    (r'^submit/(?P<entry_id>\d+)/enter/', 'enter'),
    (r'^single/(?P<entry_id>\d+)/$', 'single'),
    (r'^post/(?P<entry_id>\d+)/(?P<answer_id>\d+)/$', 'blog_post'),
    (r'^question/$', 'question'),
    (r'^question/enter/$', 'question_submit'),
    (r'^about', 'about'),
    (r'^single/(?P<entry_id>\d+)/upvote/', 'upvote'),                   
    (r'^post/(?P<entry_id>\d+)/(?P<answer_id>\d+)/upvote_post/', 'upvote_post'),
)

urlpatterns += patterns('',
    (r'^feedback/$', 'feedback.views.home'),
    (r'^feedback/submit/$', 'feedback.views.feedback_submit'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
