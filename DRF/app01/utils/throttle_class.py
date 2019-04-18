from rest_framework.throttling import BaseThrottle
from rest_framework.throttling import SimpleRateThrottle
import time
# VISIT_RECORD = {
# # }
# class VisitThrottle(BaseThrottle):
#     def __init__(self):
#         self.history = None
#     def allow_request(self, request, view):
#         '''
#         限制IP每分钟访问不能超过3次
#         :param request:
#         :param view:
#         :return:
#         '''
#         # print(self.get_ident(request)) # 获取ip地址
#         remote_addr = request.META.get('REMOTE_ADDR') # 获取ip地址
#         now = time.time()
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr]=[now,]
#             return True
#         history = VISIT_RECORD[remote_addr]
#         self.history=history
#         while history and now-history[-1] > 60:
#             history.pop()
#         if len(history)<3:
#             history.insert(0,now)
#             return True   # 返回True是继续往下进行
#         else:
#             return False
#
#     def wait(self):
#         # 当前访问时间
#         now = time.time()
#         #  访问时间历史记录 self.history
#         return 60-(now-self.history[-1])


class VisitThrottle(SimpleRateThrottle):
    scope = "visit_rate"
    def get_cache_key(self, request, view):
        return self.get_ident(request)