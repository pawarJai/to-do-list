from django.shortcuts import render,redirect
from .serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from django.views import View
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


def login(request):
    """
    This Function Is Created For Login
    """
    return render(request,"user/pages-login.html")

def user_signin(request):
    """
    This Function Is Created For User Signin
    """
    user = authenticate(username=request.POST.get("email"), password=request.POST.get('password'))
    if user is not None:
        auth_login(request, user)
        context = {
            "user": request.user
        }

        return redirect("home page")
    else:
        messages.error(request, '*Login details are not valid')
        error = "your email and password not valid"
        return render(request,"user/pages-login.html",{"error":error})

class Register(View):
    """
    This View Is Created For Register the User
    """
    def get(self,request):
        return render(request,"user/register.html")
    def post(self,request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User(
                    first_name=first_name,
                    last_name=last_name,
                    phone = phone,
                    email = email,
                    password = make_password(password) 
                    )
        user.save()
        return redirect("login")


class UserList(APIView):
    """
    This API Is Created For User Data GET,POST Opration
    """
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user = User.objects.all()
        serializer = UserSer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = UserSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    """
    This API  Is Created For Get Particular One User GET,PUT,DELETE Opration
    """
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        user = self.get_object(pk)
        serializer = UserSer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        user = self.get_object(pk=pk)
        user.delete()
        msg = {"massage":"data delete sucessfuly"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)