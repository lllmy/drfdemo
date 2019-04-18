from rest_framework.permissions import AllowAny
from rest_framework.permissions import BasePermission


class SVIPPermission(BasePermission):
    message = "您没有访问权限"

    def has_permission(self,request,view):
        if request.user.user_type >=2:
            return True
        return False