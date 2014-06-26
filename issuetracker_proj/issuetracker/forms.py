from django import forms
from .models import Issue, IssueModeration, IssueComment

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title','description', 'category',)

class IssueModerationForm(forms.ModelForm):
    class Meta:
        model = IssueModeration
        fields = ('priority','status','assigned_to')

class IssueCommentCreateForm(forms.ModelForm):
    class Meta:
        model = IssueComment
        fields = ('content',)
