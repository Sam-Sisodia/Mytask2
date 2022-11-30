from rest_framework.permissions import BasePermission
from . models import *

from rest_framework.response import Response



from rest_framework.response import Response


class UserPermission(BasePermission):
        def has_permission(self, request, view):
            try:
                user = request.user
                #print(request)
                obj = User.objects.get(username=user)
                print(obj.first_name)
                usertype = obj.usertype
            
                if request.method == "GET":
                    return True

                if request.method =="POST"  or  request.method =="PUT"  or   request.method=="DELETE": 
                    if usertype == "":
                        return True
                return False
                
            except:
                pass