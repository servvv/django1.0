from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth .forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
import os
# Create your views here.
def index(request):
    img_path=r"C:\Users\y\Desktop\graduation_project\mysite\eshop\static\image\img\270"
    img_list=os.listdir(img_path)
    context={"img":img_list}
    print(img_list)
    return  render(request,'index.html',context)

def logins(request):
    if request.method=="POST":
        user=authenticate(request,username=request.POST["username"],password=request.POST["password"])
        if user is None:
            return render(request,"login.html",{"错误":"用户名或密码错误"})
        else:
            login(request,user)

            print(user)
            return redirect(index)
    else:
        return  render(request,'login.html')
def logouts(request):
    logout(request)
    return render(request, 'index.html')
def register(request):
    if request.method=="POST":
        frome=自定义注册表单(request.POST)
        print(frome)
        if frome.is_valid():
            frome.save()
            user=authenticate(request, username=frome.cleaned_data["username"],password=frome.cleaned_data["password1"])
            user.email=frome.cleaned_data["email"]
            用户列表(username=user,昵称=frome.cleaned_data["昵称"],生日=frome.cleaned_data["生日"]).save()
            login(request,user)
            return redirect(index)

    else:
        frome=自定义注册表单()
    contexts={"register_form":frome}
    return render(request,"register.html",contexts)

@login_required(login_url="/login/")
def usercenter(request):
        # userinfo=用户列表.objects.get(request.)
        print("用户中心")
        context={"user":request.user}
        return render(request,"用户信息页.html",context)

@login_required(login_url="/login/")
def usercenter_edit(request):
    if request.method=="POST":
        frome=修改表单(request.POST,instance=request.user)
        print(frome)
        if frome.is_valid():
            frome.save()
            request.user.用户列表.昵称 = frome.cleaned_data["昵称"]
            request.user.用户列表.生日= frome.cleaned_data["生日"]
            request.user.用户列表.save()
            # user=authenticate(request, username=frome.cleaned_data["username"],password=frome.cleaned_data["password1"])
            # user.email=frome.cleaned_data["email"]
            # 用户列表(username=user,昵称=frome.cleaned_data["昵称"],生日=frome.cleaned_data["生日"]).save()
            return redirect(usercenter)
    else:
        userchange=修改表单(instance=request.user)
    context = {"changefome": userchange,"users":request.user}
    return render(request,"修改用户信息.html",context)

@login_required(login_url="/login/")
def usercenter_repassword(request):
    if request.method=="POST":
        frome=PasswordChangeForm(data=request.POST,user=request.user)
        print(frome)
        if frome.is_valid():
            frome.save()

            return redirect(logins)
    else:
        userchange=PasswordChangeForm(user=request.user)
    context = {"changefome": userchange,"users":request.user}
    return render(request,"修改密码.html",context)
def search(request):
    return render(request,"搜索页.html")