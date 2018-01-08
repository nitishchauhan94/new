

# Create your models here.
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField
from django.core.urlresolvers import reverse


class shifts(models.Model):
    days = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    names = (
        ('Akshay', 'Akshay'),
        ('Ankit', 'Ankit'),
        ('Dikshant', 'Dikshant'),
        ('Nitish', 'Nitish'),
        ('Priyanka', 'Priyanka')
    )
    # date = models.DateField(u'Day of the event', help_text=u'Day of the event')
    date = models.CharField(max_length=40)
    Day = MultiSelectField(choices=days,null=True,blank=True,max_choices=1)
    Morning = MultiSelectField(choices=names, null=True, blank=True,max_choices=1)
    Evening = MultiSelectField(choices=names, null=True, blank=True,max_choices=1)
    General = MultiSelectField(choices=names, null=True, blank=True)
    Planned = models.TextField(max_length=50, null=True, blank=True)
    Comp_off = MultiSelectField(choices=names, null=True, blank=True)
    Leave = MultiSelectField(choices=names, null=True, blank=True)

    # def __unicode__(self):,
    #      return self.day

    def get_absolute_url(self):
        return reverse("shift:detail", kwargs={"id": self.id})	
