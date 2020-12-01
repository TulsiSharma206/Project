from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('events/',views.events),
    path('home.html/',views.login),
    path('home.html/calendar/1',views.CalendarView.as_view()),
]