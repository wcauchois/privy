from django.db import models

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
    Posts
"""

"""
    Boards
"""

"""
    Location
"""

"""
    Alias
"""


