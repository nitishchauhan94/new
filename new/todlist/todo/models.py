from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Shift(models.Model):
    Date = models.CharField(max_length=40)
    Day = models.CharField(max_length=40)
    Morning = models.CharField(max_length=50,null=True)
    Evening = models.CharField(max_length=60,null=True)
    General = models.CharField(max_length=70,null=True)
    Leave = models.CharField(max_length=70,null=True)

    def __str__(self):
      return self.Date

    def get_absolute_url(self):
        return reverse("shift:detail", kwargs={"id": self.id})

	
