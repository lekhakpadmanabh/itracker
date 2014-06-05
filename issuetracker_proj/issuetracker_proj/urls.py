from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'issuetracker.views.index', name='issue_home'),
    url(r'^(?P<pk>\d+)/', 'issuetracker.views.detail', name='issue_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
