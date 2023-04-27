from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name ="home"),
    path('addUserPage/',addUserPage,name ="addUserPage"),
    path('createUser/',createUser,name ="createUser"),
    path('readUser/',readUser,name ="readUser"),
    path('readUserDetail/<int:id>/',readUserDetail,name ="readUserDetail"),
    path('editUser/<int:id>/',editUser,name ="editUser"),
    path('updateUser/<int:id>/',updateUser,name ="updateUser"),
    path('deleteUser/<int:id>/',deleteUser,name ="deleteUser"),
    path('qr_gen/<int:id>/',qr_gen,name ="qr_gen"),

]
