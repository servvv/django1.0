from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# Create your models here.
#商品类别表
class 商品类别表(models.Model):
    名称 = models.CharField(max_length=50,unique=True)#商品类别最大长度为50，且是不可重复唯一值
    类别描述 = models.TextField(blank=True)#可以为空
    图片 =models.ImageField(upload_to="category",blank=True)#上传图片到category文件夹,可以为空

    class Meta:
        verbose_name = "商品类别表"
        verbose_name_plural = "商品类别表"
        db_table="商品类别表"
    def __str__(self):
        return  self.名称

#产品列表
class 产品列表(models.Model):
    产品名称 = models.CharField(max_length=50,unique=True)#产品类别最大长度为50，且是不可重复唯一值
    产品描述 = models.TextField(blank=True)#可以为空
    产品图片 =models.ImageField(upload_to="category",blank=True)#上传图片到category文件夹,可以为空
    所属类别=models.ForeignKey(商品类别表,on_delete=models.CASCADE)#关联商品类别表的外键，串联接，连坐。当上表删除某类别数据本表数据也将被删除
    价格=models.DecimalField(max_digits=10,decimal_places=2)#max_digits最大位数，decimal_places最大小数位
    库存=models.IntegerField(default=0)#默认值为零
    已上架=models.BooleanField(default=True)
    创建时间=models.DateTimeField(auto_now_add=True)#当创建商品时自动加上当时时间可手动更改
    修改时间=models.DateTimeField(auto_now_add=True)#当修改商品时自动加上当时时间
    class Meta:
        verbose_name = "产品列表"
        verbose_name_plural = "产品列表"
        db_table="产品列表"
        ordering =('-创建时间',)
    def __str__(self):
        return  self.产品名称
class 用户列表(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    昵称=models.CharField(max_length=50,blank=True)
    生日=models.DateTimeField(blank=True,null=True)
    # 邮箱=models.EmailField()
    账户余额=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = "用户列表"
        db_table="用户列表"
    def __str__(self):
        return  self.username.username


    # 订单号=models.IntegerField()
# class 购物车(models.Model):
#     num=models.IntegerField(default=1)
#     产品 = models.ForeignKey(产品列表,on_delete=models.CASCADE)
#     用户id=models.ForeignKey(用户列表,on_delete=models.)
#
#
#     class Meta:
#         verbose_name = "购物车"
#         verbose_name_plural = "购物车表"
#         db_table = "别购物车表"
#
#     def __str__(self):
#         return self.名称
