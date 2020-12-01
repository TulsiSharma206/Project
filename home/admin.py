from django.contrib import admin
from .models import Home
from .models import Event
from django_admin_relation_links import AdminChangeLinksMixin
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar


@admin.register(Home)
class HomeAdmin(AdminChangeLinksMixin,admin.ModelAdmin):
      list_display = ['username']
      changelist_links = ['events'] # Use the `related_name` of the `Event.Home` field

global extra_context
@admin.register(Event)
class EventAdmin(AdminChangeLinksMixin,admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']
    change_links = ['Event_name']  # Just specify the name of the `ForeignKey` field
    change_list_template ='view_calendar.html'
    
    def changelist_view(self, request, extra_context=None):
            extra_context = {}
            after_day = request.GET.get('day__gte', None)
            if not after_day:
                  d = datetime.date.today()
            else:
                  try:
                       split_after_day = after_day.split('-')
                       d = datetime.date(year=int(split_after_day[0]), month=int(split_after_day[1]), day=1)
                  except:
                       d = datetime.date.today()
            
            previous_month = datetime.date(year=d.year, month=d.month, day=1)  # find first day of current month
            previous_month = previous_month - datetime.timedelta(days=1)  # backs up a single day
            previous_month = datetime.date(year=previous_month.year, month=previous_month.month,
                                       day=1)
            
            last_day = calendar.monthrange(d.year, d.month)
            
            # find last day of current month
            next_month = datetime.date(year=d.year, month=d.month, day=last_day[1])  
            
            # forward a single day
            next_month = next_month + datetime.timedelta(days=1)  
            
            # find first day of next month
            next_month = datetime.date(year=next_month.year, month=next_month.month,
                                   day=1)  
            #events/templates/admin/events/change_list.html
            #extra_context['previous_month'] = reverse('admin:event_changelist') + '?day__gte=' + str(previous_month)
            #extra_context['next_month'] = reverse('admin:event_changelist') + '?day__gte=' + str(next_month)

            cal = EventCalendar()
            html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
            html_calendar = html_calendar.replace('<td ', '<td  width="150" height="150"')
            extra_context['calendar'] = mark_safe(html_calendar)
            return super(EventAdmin, self).changelist_view(request, extra_context)

            

