from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from issuetracker.api import IssueResource

v1_api = Api(api_name='v1')
v1_api.register(IssueResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^issue/', include('issuetracker.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/','login',
    {'template_name': 'login.html'},
    name='issue_login'),
    
    url(r'^logout/','logout',
    {'next_page': 'issue_home'},
    name='issue_logout'),
)
