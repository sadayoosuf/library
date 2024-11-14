from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from users.models import Users,CustomUser


def adminregister(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        a=request.POST['a']
        n=request.POST['n']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,Address=a,phone=n,is_superuser=True)
            u.save()
        else:
            return HttpResponse("password are not matching")
        return redirect('users:login')
    return render(request,'adminregister.html')

def userregister(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        a=request.POST['a']
        n=request.POST['n']

        if(p==cp):
            u=CustomUser.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e,Address=a,phone=n,is_user=True)
            u.save()
        else:
            return HttpResponse("password are not matching")
        return redirect('users:login')
    return render(request,'userregister.html')


def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_superuser == True:
            login(request,user)

        elif user and user.is_user == True:
            login(request,user)

        else:
            return HttpResponse("invalid user")

        return redirect('books:home')



    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('users:login')

@login_required
def view_users(request):
    k=Users.objects.all()
    context={'user':k}
    return render(request,'view_users.html',context)
