from django.db import models
from datetime import *

class Board(models.Model):
  radius = models.DecimalField(max_digits=15, decimal_places=5)
  center_lat = models.DecimalField(max_digits=15, decimal_places=5)
  center_lng = models.DecimalField(max_digits=15, decimal_places=5)
  name = models.CharField(max_length=255)

class Post(models.Model):
  locale = models.ForeignKey(Board, blank=False)
  date_created = models.DateTimeField(editable=False)
  content = models.TextField(null=True, blank=False)

  def save(self):
    if self.date_created == None:
      self.date_created = datetime.now()
    super(Post, self).save()

