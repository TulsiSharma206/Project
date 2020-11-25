from django.shortcuts import render
from django.http import HttpResponse
from .models import Home
from django.shortcuts import get_object_or_404

def home(request):
    if request.method == 'POST':
        username1=request.POST.get('uname')
        password1=request.POST.get('psw')
        users=Home.objects.all()
        flag=0
        for u in users:
             if(u.username == username1):
                 if(u.password == password1):
                     flag=1
                     name=u.username
                     user=Home.objects.get(username=name)
                     return render(request, 'login.html', { 'user': user})
        if flag == 0:
            #return render(request,'home.html')
            return HttpResponse('invalid')
    else:
        return render(request,'home.html')
