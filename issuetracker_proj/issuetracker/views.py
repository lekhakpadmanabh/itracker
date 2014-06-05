from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Issue
from .forms import IssueForm
""" FBV to be changed """

def index(request):
    if request.method == 'POST':
        form = IssueForm(data = request.POST)
        if form.is_valid():
            new_issue = form.save()
            return HttpResponseRedirect(reverse(
                'issue_detail',
                args = (new_issue.pk,)))

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
