#!usr/bin/env python
#-*- coding:utf-8 _*-
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
#coding:utf-8

class 自定义注册表单(UserCreationForm):
    昵称 =forms.CharField(max_length=50,required=False)
    生日 = forms.DateTimeField(required=False)
    # 邮箱 = forms.EmailField(required=False)
    class Meta:
        model=User
        fields=("username","password1","password2","email","昵称","生日")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].error_messages = {"unique": "用户名已存在!!!", "invaild": "格式不对,请重新输入"}

class 修改表单(UserChangeForm):
    昵称 = forms.CharField(max_length=50, required=False)
    生日 = forms.DateTimeField(required=False)
    # 邮箱 = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ("username","email", "password","昵称", "生日")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].error_messages = {"unique":"用户名已存在!!!","invaild":"格式不对,请重新输入"}
# class 修改密码(UserChangeForm):
#
#
#     # 邮箱 = forms.EmailField(required=False)
#     class Meta:
#         model = User
#         fields = ("username", "email", "password", "昵称", "生日")
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["username"].error_messages = {"unique": "用户名已存在!!!", "invaild": "格式不对,请重新输入"}


