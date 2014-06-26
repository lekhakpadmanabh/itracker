from django.conf.urls import patterns, url
from issuetracker.views import IssueListView, IssueDetailView, IssueCreateView, \
    IssueUpdateView, IssueCommentCreateView, IssueNotificationsView, IssueModerationView

urlpatterns = patterns('',
    #url(r'^$', views.index, name='issue_home'),
    url(r'^$', IssueListView.as_view(), name='issue_home'),
    url(r'^(?P<pk>\d+)/', IssueDetailView.as_view(), name='issue_detail'),
    url(r'^edit/(?P<pk>\d+)', IssueUpdateView.as_view(), name='issue_update'),
    url(r'^new/', IssueCreateView.as_view(), name='issue_create'),
    url(r'^comment/new/(?P<pk>\d+)', IssueCommentCreateView.as_view(), name='issue_comment_create'),
    url(r'^notifications/', IssueNotificationsView.as_view(),name='issue_notifications_list'),
    url(r'^moderate/(?P<issue_id>\d+)', IssueModerationView.as_view(),name='issue_moderation')
    #url(r'^itmod/(?P<pk>\d+)/', views.itmod_set, name='itmod_set')
    
)
