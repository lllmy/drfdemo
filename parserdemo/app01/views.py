from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.


class LoginView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        #两种方式比较
        # 第一种方式：form 表单提交默认的编码格式就是urlencoded
        print(request.body)  # 请求体中的原生数据
        # b'csrfmiddlewaretoken=lARJZnHAKoJrffG0gQcLuuGsNzpFn609QkEYhUOzCR2IaJjtLOIYBKYmEmIdm4rp&user=luhan&pwd=1234'
        print(request.POST)
        # < QueryDict: {'pwd': ['1234'], 'user': ['luhan'],
        #               'csrfmiddlewaretoken': ['lARJZnHAKoJrffG0gQcLuuGsNzpFn609QkEYhUOzCR2IaJjtLOIYBKYmEmIdm4rp']} >
        # 第二种方式：ajax 表单提交默认的编码格式为json
        # b'{"user":"luhan","pwd":"123456"}'
        print(request.body)  # 请求体中的原生数据
        print(request.POST)
        import json
        print(json.loads(request.body.decode("utf8")))
        # {'user': 'luhan', 'pwd': '123456'}
        print(json.loads(request.body.decode("utf8"))["user"])
        # luhan
        # print(type(request))
        # < QueryDict: {} >
        from django.core.handlers.wsgi import WSGIRequest
        return HttpResponse("OOK")