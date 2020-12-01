from django.shortcuts import render
from django.http import HttpResponse
from .models import Home,Event
from django.shortcuts import get_object_or_404
from datetime import date,time,datetime
import calendar
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .admin import EventAdmin
from django.urls import reverse_lazy
from django.views.generic import ListView
from datetime import datetime,date,time,timedelta
from .utils import EventCalendar
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def home(request):
        return render(request,'choice.html')

def login(request):

   if 'login' in request.POST:
            return render(request,'home.html')    
   elif 'Signin' in request.POST:
                username1=request.POST.get('uname')
                password1=request.POST.get('psw')
                user = authenticate(username=username1, password=password1)
                if user is not None:
                     H=Home.objects.get(username='tulsisharma')
                     U=User.objects.get(username=username1)
                     context= {
                                   'H': H,
                                   'U': U,
                              }
                     return render(request, 'login.html', context)
                else:
                     return HttpResponse("invalid "+username1+" or password "+password1) 

      
                                
def events(request):
    return render(request,'view_calendar.html')

class CalendarView(ListView):
     model = Event
     template_name = 'calendar.html'
     
     
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          d = get_date(self.request.GET.get('month', None))
          cal = EventCalendar()
          html_cal = cal.formatmonth(d.year,d.month)
          context['calendar'] = mark_safe(html_cal)
          #context['prev_month'] = prev_month(d)
          #context['next_month'] = next_month(d)
          #return render (request, 'calendar.html', {'context': context})
          return context




def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime(year, month, day=1)
    return datetime.today() 


  


