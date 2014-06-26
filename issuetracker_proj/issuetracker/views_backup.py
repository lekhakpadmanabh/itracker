from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Issue, IssueModeration
from .forms import IssueForm, IssueModerationForm
from django.contrib.auth.models import User

""" FBV to be changed """

def index(request):
    if request.method == 'POST':
        author = Issue(author=request.user)
        form = IssueForm(data=request.POST, instance=author)
        if form.is_valid():
            new_issue = form.save()
            return HttpResponseRedirect(reverse(
                'issue_detail',
                args = (new_issue.pk,)))
        else:
            return HttpResponse('something form not right')
    else:
        issues = Issue.objects.all()
        form = IssueForm()
        return render(request,
            'issuetracker/index.html',
            {'issues': issues,
             'form': form},
            )

def detail(request,pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request,
        'issuetracker/detail.html',
        {'issue': issue},
        )

def itmod_set(request, pk):
    """
    Bug: whenever I try to set mods for
    an issue where mods have already been set, 
    I get the integrity error because it already exists.
    How to edit an existing field?
    """
    if request.method == 'POST':
        mod_issue = IssueModeration.objects.get(pk=pk)
        issue = Issue.objects.get(pk=pk)
        mod_form  = IssueModerationForm(request.POST, instance=mod_issue)
        if mod_form.is_valid():
            #cd = mod_form.cleaned_data
            newmodset = IssueModeration(
                issue = issue,
                priority = request.POST['priority'],
                status = request.POST['status'],
                assigned_to = get_object_or_404(User,pk=request.POST['assigned_to'])
            )
            newmodset.save()
            HttpResponseRedirect(reverse(
                'issue_detail',
                args = (mod_issue.pk,)))
        else:
            return HttpResponse('invalid input')
    else:
        mod_issue = IssueModeration.objects.get(pk=pk)
        mod_form = IssueModerationForm(instance = mod_issue)
        return render(request,
            'issuetracker/modform.html',
            {'mod_form': mod_form},
            )
