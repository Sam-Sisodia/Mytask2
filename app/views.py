from django.shortcuts import render

from . models import *
from .serializer import *
from  rest_framework.viewsets import ModelViewSet

# Create your views here.
from functools import partial
from django.shortcuts import render
from rest_framework .views import APIView
from . serializer import *
from . models import *
from rest_framework import status
 
from  rest_framework.viewsets import ModelViewSet
 
from rest_framework.response import Response  
from django.contrib.auth import authenticate , login , logout
from rest_framework.generics import CreateAPIView


class registerUsereView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Registerserilizer
    def post(self,request,*args, **kwargs):
        serializer = Registerserilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #password = serializer.validated_data['password']
            user = serializer.save()
    
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class (CreateView):

class Loginview(CreateAPIView):
    queryse = User.objects.all()
    serializer_class  = LogSerializer
    
    def post(self,request, *args, **kwargs):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
               login(request,user)
               return Response( status=status.HTTP_200_OK)

            if user is  None:
                 return Response( status=status.HTTP_400_BAD_REQUEST,)






class SchoolDetails(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = Schoolserilizer
   # permission_classes =[ UserPermission,IsAuthenticated]


class Classdetails(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = classSerilizer
    search_fields = ['id']
   # permission_classes =[ UserPermission,IsAuthenticated]




class TeacherDetails(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerilizer

   # permission_classes =[ UserPermission,IsAuthenticated]



class Studentdetails(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserilizer
    #permission_classes =[ UserPermission,IsAuthenticated]

class Userdetails(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserlizer














