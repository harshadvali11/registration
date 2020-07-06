from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    if request.session.get('username'):
        user=request.session.get('username')
        return render(request,'home.html',context={'user':user})
    return render(request,'home.html')


def register(request):
    userform=UserForm()
    profileform=ProfileForm()
    register=False
    
    if request.method=='POST' and request.FILES:
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            user.save()
            profile=profileform.save(commit=False)
            profile.user=user
            profile.save()
            send_mail('Registration',
                      'Thanks for registering,ur registration is successfull',
                      'harshadvali09@gmail.com',
                      [user.email],
                      fail_silently=False,
                    
                    )

            register=True
            
    d={'userform':userform,'profileform':profileform,'register':register}
    return render(request,'register.html',context=d)


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))

    return render(request,'user_login.html')









