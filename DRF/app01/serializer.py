
from rest_framework import serializers

from app01.models import *

# Create your views here.
# 用最为普通的方式自己写
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.DecimalField(max_digits=5,decimal_places=2)
#     # 一对多字段
#     publish_name = serializers.CharField(max_length=32,source="publish.name")
#     publish_email=serializers.CharField(max_length=32,source="publish.email")
#     # 多对多字段
#     # authors = serializers.CharField(max_length=32,source="authors.all")
#     # 这样写给前端造成了巨大的困扰
#     authors = serializers.SerializerMethodField()
#     def get_authors(self,obj):
#         ret = []
#         for i in obj.authors.all():
#             ret.append(i.name)
#         return ret

# 用ModelSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    # 我们想要出版社的名字
    # publish = serializers.CharField(max_length=32, source="publish.name")
    # # 想要作者的名字和id呢
    # authors=serializers.SerializerMethodField()
    # def get_authors(self,obj):
    #     ret=[]
    #     for i in obj.authors.all():
    #         ret.append({"name":i.name,"pk":i.pk})
    #     return ret


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"