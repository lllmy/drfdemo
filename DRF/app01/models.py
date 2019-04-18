from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=64)

class User(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    type=((1,"VIP"),(2,"SVIP"),(3,"SSSVIP"))
    user_type=models.IntegerField(choices=type)


class UserToken(models.Model):
    user=models.OneToOneField("User")
    token=models.CharField(max_length=128)

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    age=models.IntegerField()

    def __str__(self):
        return self.name


class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors=models.ManyToManyField(to='Author',)