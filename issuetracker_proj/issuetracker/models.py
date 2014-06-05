from django.db import models

class CategoryManager(models.Manager):
    def water_count(self):
        return super(CategoryManager, self).get_query_set().filter(category='W').count()

class Issue(models.Model):
    CATEGORIES = (
        ('W', 'Water'),
        ('R', 'Road'),
        ('E', 'Electricity'),
        ('G', 'Garbage'),
    )
    PRIORITY = (
        ('H', 'High'),
        ('M', 'Med'),
        ('L', 'Low'),
    )
    REASON_FOR_CLOSING = (
        ('R', 'Resolved'),
        ('M', 'Merged'),
        ('S', 'Spam'),
    )
    title = models.CharField(max_length=140)
    description = models.TextField()
    category = models.CharField(max_length=1,
        choices=CATEGORIES)
    priority = models.CharField(max_length=1,
        choices=PRIORITY,
        blank=True)
    status = models.BooleanField(default=True,
        help_text="""
        True: Open
        False: Closed
        """)
    reason_for_closing = models.CharField(max_length=1,
        choices=REASON_FOR_CLOSING,
        blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    cat = CategoryManager()
    def __unicode__(self):
        return self.title
