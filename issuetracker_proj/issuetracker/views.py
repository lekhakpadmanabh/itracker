from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Issue, IssueModeration, IssueComment
from .forms import IssueForm, IssueModerationForm, IssueCommentCreateForm
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, TemplateView

class IssueListView(ListView):
    """ Displays list of all issues
    on app home page, along with
    new issue submit form. """

    model = Issue
    template_name = 'issuetracker/index.html'
    context_object_name = 'issues'
    paginate_by = 5
    success_url = '/issue/'

    def get_context_data(self,*args,**kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        context['issueform'] = IssueForm()
        return context

class IssueDetailView(DetailView):
    """ Displays issue details along
    with comments and moderation tools."""

    model = Issue
    template_name = 'issuetracker/detail.html'
    context_object_names = 'issue'

    def get_context_data(self,*args,**kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['commentform'] = IssueCommentCreateForm()
        return context

class IssueCreateView(CreateView):
    """View for new issue form, notice
    that a template has been provided even 
    though the form appears in IssueListView.
    Any errors in the form will redirect to this
    template."""

    form_class = IssueForm
    template_name= 'issuetracker/new_issue.html'

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        self.object = obj
        return HttpResponseRedirect(self.get_success_url())

class IssueUpdateView(UpdateView):
    """Updates existing issue. Permissions
    (i.e only author can update issue) are handled
    on the template side. Not sure if its a good thing."""

    model = Issue
    fields = ['title','description','category']
    template_name = 'issuetracker/edit_issue.html'

class IssueCommentCreateView(CreateView):
    model = IssueComment
    template_name = 'issuetracker/new_comment.html'
    fields = ['content']

    def form_valid(self, form):
        parent_issue = Issue.objects.get(pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.issue = parent_issue
        return super(IssueCommentCreateView, self).form_valid(form)

class IssueModerationView(UpdateView):
    """Displays moderation fields, which were
    automatically set to default values upon
    creation of the issue instance via signals"""

    slug_field = 'issue_id'
    slug_url_kwarg = 'issue_id'
    model = IssueModeration
    template_name = 'issuetracker/moderate.html'
    fields = ['priority','status','assigned_to']

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.kwargs['issue_id']})



class IssueNotificationsView(TemplateView):
    """Displays all read and unread notifications
    for a user and changes the viewed field to true"""

    template_name='issuetracker/notifications.html'

    def get_context_data(self, **kwargs):
        """ Not sure if this is the right way to
        add context. Could be better. """
        user = self.request.user
        user_unread = user.issuenotification_set.filter(viewed=False)
        user_read = user.issuenotification_set.filter(viewed=True)
        context = super(IssueNotificationsView, self).get_context_data(**kwargs)
        context.update({'user_unread': user_unread, 'user_read': list(user_read)})
        for msg in user_unread:
            msg.viewed = True
            msg.save()
        return context
