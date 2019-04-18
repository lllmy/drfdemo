from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from app01.models import Book, Publish, Author
from app01.serializer import BookSerializer, PublishSerializer,AuthorSerializer
from app01.utils.auth_class import UserAuth
import time
from app01.utils.permission_class import SVIPPermission
from app01.utils.throttle_class import VisitThrottle
from rest_framework.renderers import BrowsableAPIRenderer,JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser,JSONParser
############Book

class BooksView(APIView):
    parser_classes = [FormParser,JSONParser]
    authentication_classes = [UserAuth]
    permission_classes = [SVIPPermission]
    throttle_classes = [VisitThrottle]
    renderer_classes = []
    def get(self, request):
        '''
        查看多条数据
        :param request:
        :return:
        '''
        # print(request.user,request.auth)
        class MyPageNumberPagination(PageNumberPagination):
            page_size = 3  # 每页的显示的个数
            page_query_param = "page_num"  # 手动点击第几页
            page_size_query_param = "size"  # size手动是一页显示的个数
            max_page_size = 5   # 最大的页显示的个数

        book_list = Book.objects.get_queryset().order_by("nid")
        pnp = MyPageNumberPagination()
        paged_book_list = pnp.paginate_queryset(book_list,request)
        serializer = BookSerializer(paged_book_list, many=True)
        '''
        具体操作解析，就是怎么序列化的：
        serializer=BookSerializer(book_list,many=True)
        serializer.data:
        temp=[]
        for obj in book_list:
        temp.append({
         "title":obj.title,
         "price":obj.price,
         "publish":obj.publish.email,
         if 字段SerializerMethodField：
         "authors":get_authors(obj)
    })
        json.dumps(temp)

        '''
        return Response(serializer.data)

    def post(self, request):
        '''
        提交数据添加一条书籍
        :param request:
        :return:
        '''
        print(request.data)
        serializer = BookSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()  # 保存到数据库中 create操作
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class SBookView(APIView):
    def get(self, request, id):
        '''
        查看一条数据
        :param request:
        :param id:
        :return:
        '''
        show_obj = Book.objects.get(pk=id)
        serializer = BookSerializer(show_obj, many=False)
        # 返回查看的单条数据
        return Response(serializer.data)

    def put(self, request, id):
        '''
        更新一条数据update
        :param request:
        :param id:
        :return:
        '''
        edit_obj = Book.objects.get(pk=id)
        serializer = BookSerializer(data=request.data, instance=edit_obj)
        if serializer.is_valid():
            serializer.save()
            # 返回更新后的数据
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        '''
        删除一条数据
        :param request:
        :param id:
        :return:
        '''
        edit_obj = Book.objects.get(pk=id).delete()
        # 返回空
        return Response("")


#PublishView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin


class PublishView(ListModelMixin,CreateModelMixin,generics.GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SPublishView(UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,generics.GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# AuthorsView
# class AuthorsView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class SAuthorsView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

from rest_framework.viewsets import ModelViewSet


class AuthorsView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


from app01.models import User,UserToken
class LoginView(APIView):
    '''
    1000:成功
    1001:用户名或者密码错误
    1002:异常错误
    '''
    def post(self,request):
        response = {"code":1000,"msg":None,"user":None}
        try:
            print(request.data)
            user = request.data.get("user")
            pwd = request.data.get("pwd")
            user = User.objects.filter(user=user,pwd=pwd).first()
            import uuid
            random_str = uuid.uuid4()
            if user:
                UserToken.objects.update_or_create(user=user,defaults={"token":random_str})
                response["user"]=user.user
                response["token"] = random_str
            else:
                response["code"] = 1001
                response["msg"] = "用户名或者密码错误"
        except Exception as e:
            response["code"] = 1002
            response["msg"] = str(e)

        return Response(response)