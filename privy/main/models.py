from django.db import models
from datetime import *

"""
    Defines an abstract model with timestamps for creation and modification.
"""
class TimeStampedModel(models.Model):
    date_created = models.DateTimeField(editable=False)
    date_modified = models.DateTimeField(editable=False)

    def save(self):
        if self.date_created == None:
            self.date_created = datetime.now()
        self.date_modified = datetime.now()
        super(TimeStampedModel, self).save()

    class Meta:
        abstract = True


"""
    Named, dated content.
"""

class NamedDatedContent(TimeStampedContent):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def save(self):
        super(NamedDatedContent, self).save()

    class Meta:
        abstract = True


class PrivyContent(NamedDatedContent):
    connection_name = 'privy_content'

    def save(self):
        super(PrivyContent, self).save()

    class Meta:
        abstract = True


"""
    Post
"""

class Post(PrivyContent):
    locale = models.ForeignKey(blank=True, null=True)
    source_link = models.TextField(blank=True, null=True) 
    creator = models.ForeignKey()
    locale = models.ForeignKey()

    def __unicode__(self):
        return "[id: '%s', name: '%s']" % (self.id, self.name[:27] +'...') 

    class Meta:
        db_table = 'dashboard_dashboard';


"""
    Locale
"""
class Locale(PrivyContent):
    radius = models.DecimalField(max_digits=15, decimal_places=5)
    center_x = models.DecimalField(max_digits=15, decimal_place=5)
    center_y = models.DecimalField(max_digits=15, decimal_place=5)
    creator = models.ForeignKey()
    # institution = models.ForeignKey(null=True, blank=True)

"""
    Alias
""" 
class Alias(PrivyContent):
    # institution = models.ForeignKey(null=True, blank=True)
