from django import template

register = template.Library()

@register.simple_tag(name="unread")
def get_unread_notifications_user(user):
    return user.issuenotification_set.filter(viewed=False).count()
