# 认证权限
from app01.models import UserToken

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
# 导入这个base....是因为要有authenticate_header这方法，虽然没怎么用，但是得有。这样省的我们自己写

class UserAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        usertoken = UserToken.objects.filter(token=token).first()
        if usertoken:
            return usertoken.user,usertoken
        else:
            raise AuthenticationFailed("认证失败啦！！！")