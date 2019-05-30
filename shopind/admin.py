from django.contrib import admin
from  .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
# admin.site.register(商品类别表)
# admin.site.register(产品列表)
class 商品类别表Admin(admin.ModelAdmin):
    list_display = ["id","名称","图片"]



admin.site.register(商品类别表,商品类别表Admin)
class 产品列表Admin(admin.ModelAdmin):
    list_display = ["id","产品名称","所属类别","产品图片","价格","库存","已上架","创建时间","修改时间"]
    list_editable = ["产品名称","所属类别","产品图片","价格","库存","已上架"]#显示页面可编辑
    list_per_page = 10 #一页显示数量

admin.site.register(产品列表,产品列表Admin)
class 用户列表Inline(admin.TabularInline):
    model = 用户列表
    can_delete = False
    verbose_name_plural = "用户列表"
class UserAdmin(BaseUserAdmin):
    inlines =(用户列表Inline,)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)








































