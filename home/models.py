from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.urls import reverse
import re
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


#import datetime
#from django.urls import reverse
class Home(models.Model):
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100, blank=False )
    password = models.CharField( max_length=100, blank=False )
    SEX_CHOICES = [('M','Male'), ('F','Female')]
    Phone_number = PhoneNumberField(blank=True)
    Email = models.CharField( max_length=100, blank=True )
    Designation = models.CharField( max_length=100, blank=True)
    sex = models.CharField( max_length=1,choices= SEX_CHOICES, blank=True )


class Event(models.Model):
    #id=models.IntegerField()
    Event_name= models.ForeignKey(Home, to_field='id',on_delete=models.SET_NULL,blank=True,null=True,related_name='events')
    day = models.DateField(u'Day of the event', help_text=u'Day of the event', blank=True, default="",)
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time', default="",)
    end_time = models.TimeField(u'Final time', help_text=u'Final time',default="",)
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True, default="",)
    title = models.CharField(max_length=200,default='title')

    def __str__(self):
        return self.title
    
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))  
        return f'<p>{self.title}</p>'
        #<a href="{url}">edit</a>' 

    
    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    
    
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
 
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
    

