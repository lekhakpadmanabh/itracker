from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import IssueComment, Issue, IssueNotification, IssueModeration

"""
Shifted this from model.py
by importing this module in
the project's __init__.py
"""

@receiver(post_save, sender=IssueComment)
def notify_on_comment(sender, **kwargs):
    if kwargs.get('created', False):
        msg = "New comment posted for issue {0}".format(kwargs.get('instance').issue.title)
        sent_to = kwargs.get('instance').issue.author
        mod_tool = IssueNotification.objects.create(message=msg,notification_for_user=sent_to)


@receiver(post_save, sender=Issue)
def my_handler(sender, **kwargs):
    if kwargs.get('created', False):
        mod_tool = IssueModeration.objects.create(issue=kwargs.get('instance'))
