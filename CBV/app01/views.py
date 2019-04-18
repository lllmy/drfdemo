from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Course,Book,Publish,Author
import json
from rest_framework.parsers import JSONParser,FormParser,FileUploadParser

from rest_framework.views import APIView


# Create your views here.


class Login(View):
    def get(self, requesst):
        pass

    def post(self, request):
        pass

#
# ###################### 基于DRF的接口设计#######################
from rest_framework import serializers
from rest_framework.response import Response
class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)
    desc = serializers.CharField(max_length=32)
class Courses(APIView):
    parser_classes = []
    def get(self, request):
        '''
        get请求查看看数据的有三种方式
        :param request:
        :return:方式1：
        '''
        course_list = Course.objects.all()
        ret = []
        for course in course_list:
            ret.append({
                "title": course.title,
                "desc": course.desc
            })
        '''
        方式2：
        '''
        # from django.core.serializers import serialize  # Django的序列化组件
        # data = serialize("json",course_list)
        # print("data",data)
        '''
        [{"model": "app01.course", "pk": 1, "fields": {"title": "\u9547\u9b42", "desc": "\u5144\u5f1f\u60c5"}},
         {"model": "app01.course", "pk": 2, "fields": {"title": "\u6740\u7834\u72fc", "desc": "\u7236\u5b50\u60c5"}}]
        '''
        '''
        方式3：RestFramework序列化组件
        '''
        course_list = Course.objects.all()
        cs = CourseSerializer(course_list,many=True)
        print("**********",cs.data)
        '''
        这是一个字典
        **********
        [OrderedDict([('title', '镇魂'), ('desc', '兄弟情')]), OrderedDict([('title', '杀破狼'), ('desc', '父子情')])]
        '''
        return Response(cs.data)
        # return HttpResponse(json.dumps(ret, ensure_ascii=False))

    def post(self, request):
        # 新的request，不论是json还是urlencoded都可以解析成字典的格式
        print(request.data)  # data是静态方法：解析数据工作
        cs=CourseSerializer(data=request.data)
        if cs.is_valid():  # 校验
            Course.objects.create(**request.data)  # 填写数据库是字典的格式要打散
            return Response(cs.data)   # 序列化数据，cs.data是字符串
        else:
            return Response(cs.errors)  # 序列化错误信息


# class BooksView(APIView):
#     def get(self,request):
#         book_list = Book.objects.all()
        #RestFramework序列化组件