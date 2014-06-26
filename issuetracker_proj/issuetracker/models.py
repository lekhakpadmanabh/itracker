from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class CategoryManager(models.Manager):
    def frontend_count(self):
        return super(CategoryManager, self).get_query_set().filter(category='F').count()

class Issue(models.Model):
    CATEGORIES = (
        ('F', 'Frontend'),
        ('B', 'Backend'),
        ('U', 'UX/Design'),
        ('C', 'CRM'),
    )
    title = models.CharField(max_length=140)
    description = models.TextField()
    author = models.ForeignKey(User)
    category = models.CharField(max_length=1,
        choices=CATEGORIES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    cat = CategoryManager()

    class Meta:
        ordering = ['-date_modified']

    def get_absolute_url(self):
        return reverse('issue_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title

class IssueModeration(models.Model):
    PRIORITY = (
        ('C', 'Critical'),
        ('H', 'High'),
        ('M', 'Med'),
        ('L', 'Low'),
    )
    STATUS = (
        ('O', 'Open'),
        ('R', 'Closed: Resolved'),
        ('M', 'Closed: Merged'),
        ('W', 'Closed: Wont Fix'),
        ('S', 'Closed: Spam'),
    )
    issue = models.OneToOneField(Issue)
    priority = models.CharField(max_length=1,
        choices=PRIORITY,
        blank=True)
    status = models.CharField(max_length=1,
        choices=STATUS,
        default='O',
        blank=True)
    assigned_to = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return self.issue.title

class IssueComment(models.Model):
    issue = models.ForeignKey(Issue)
    content = models.TextField()
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('issue_detail', kwargs={'pk': self.issue.pk})

    def __unicode__(self):
        return "{1}'s comment on {0}".format(self.issue,self.author)

class IssueNotification(models.Model):
    message = models.TextField()
    notification_for_user = models.ForeignKey(User)
    viewed = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0}: {1}".format(self.notification_for_user,self.message)










