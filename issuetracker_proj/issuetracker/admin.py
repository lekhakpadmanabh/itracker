from django.contrib import admin
from .models import Issue, IssueModeration, IssueComment, IssueNotification

class IssueAdmin(admin.ModelAdmin):
    pass
admin.site.register(Issue, IssueAdmin)

class IssueModerationAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssueModeration,IssueModerationAdmin)

class IssueCommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssueComment,IssueCommentAdmin)

class IssueNotificationAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssueNotification,IssueNotificationAdmin)
