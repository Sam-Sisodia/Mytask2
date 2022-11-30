from django.contrib import admin
from django.urls import path,include

from app import views


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('schoollist',views.SchoolDetails , basename="schools")

router.register('class',views.Classdetails , basename="classes")
router.register('teacher',views.TeacherDetails , basename="teachers")

router.register('students',views.Studentdetails , basename="students")

router.register('user',views.Userdetails , basename="users")



urlpatterns = [
    
    path ('', include(router.urls)),
]
