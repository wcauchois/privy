from django.db import models
from datetime import *

class Locale(models.Model):
  radius = models.DecimalField(max_digits=15, decimal_places=5)
  center_x = models.DecimalField(max_digits=15, decimal_places=5)
  center_y = models.DecimalField(max_digits=15, decimal_places=5)

class Post(models.Model):
  locale = models.ForeignKey(Locale, blank=False)
  date_created = models.DateTimeField(editable=False)
  content = models.TextField(null=True, blank=False)

  def save(self):
    if self.date_created == None:
      self.date_created = datetime.now()
    super(Post, self).save()

