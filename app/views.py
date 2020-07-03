from django.shortcuts import render
from app.forms import *
# Create your views here.
def home(request):
    return render(request,'home.html')

'''
def register(request):
    userform=UserForm()
    profileform=ProfileForm()
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





    d={'userform':userform,'profileform':profileform}
    return render(request,'register.html',context=d)
'''
'''
def register(request):
    userform=UserForm()
    profileform=ProfileForm()
    if request.method=='POST' and request.FILES:
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save(commit=False)
            user.set_password(username.cleaned_data.get('password'))
            user.save()
            profile=profileform.save(commit=False)
            profile.user=user
            profile.save()

    d={'userform':userform,'profileform':profileform}
    return render(request,'register.html',context=d)

'''
def register(request):
    userform=UserForm()
    profileform=ProfileForm()
    
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
            
    d={'userform':userform,'profileform':profileform}
    return render(request,'register.html',context=d)












