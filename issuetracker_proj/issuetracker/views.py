from django.shortcuts import render, get_object_or_404
from .models import Issue
""" FBV to be changed """

def index(request):
    issues = Issue.objects.all()
    return render(request,
        'issuetracker/index.html',
        {'issues': issues},
        )

def detail(request,pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request,
        'issuetracker/detail.html',
        {'issue': issue},
        )
