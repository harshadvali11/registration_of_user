from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail

from app.forms import *
from django.http import HttpResponse
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('REgsitration',
                        'thank u for regsitration',
                        'hs8770164@gmail.com',
                        [MUFDO.email],
                        fail_silently=False,
                        
            )
            return HttpResponse('Registration is Successfull')
        else:
            return HttpResponse('Invalid data')







    return render(request,'registration.html',d)