from pydoc import describe
from django.shortcuts import render,redirect
from .serializer import *
from .models import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.views.generic.edit import FormView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class Home_page(View):
    """
    This View Is Created For Home Page
    """
    def get(self,request):
        to_do_list = To_Do_List.objects.filter(user__id = request.user.id)
        user_data = User.objects.get(id=request.user.id)
        return render(request,"to_do_list/index.html",{"todolist":to_do_list,"user_data":user_data})


class UserUpdate(FormView):
    template_name = "to_do_list/updatetodolist.html"
    
    def get_context_data(self, **kwargs):
        context = {
            "todolist":To_Do_List.objects.get(pk=self.kwargs["pk"]),
            "category":Category.objects.all(),
            "user_data":User.objects.filter(id=self.request.user.id),
            "status":Status.objects.all(),
        }
        return context

    def post(self,request,*args,**kwargs):
        obj = To_Do_List.objects.filter(pk=self.kwargs["pk"])
        data = request._get_post().dict()
        del data['csrfmiddlewaretoken']
        obj.update(**data)
        return redirect("home page")
        
class DeleteTodolist(FormView):

    def post(self, request, *args, **kwargs):
        obj = To_Do_List.objects.filter(pk=self.kwargs['pk'])
        data = request._get_post().dict()
        del data['csrfmiddlewaretoken']
        obj.delete()
        return redirect("home page")

class AddToDoList(View):
    """
    Add To Do List
    """
    def get(self,request):
        user = User.objects.filter(id=request.user.id)
        category =  Category.objects.all()
        status = Status.objects.all()
        return render(request,"to_do_list/add_to_do_list.html",{"user":user,"category":category,"status":status})
    
    def post(self,request):
        title = request.POST.get("title")
        discription = request.POST.get("description")
        category = request.POST.get("category")
        user = request.POST.get("user")
        date = request.POST.get("date")
        status = request.POST.get("status")

        to_do_list = To_Do_List(
                            title=title,
                            description=discription,
                            category=Category.objects.get(id=category),
                            user=User.objects.get(id=user),
                            date = date,
                            status=Status.objects.get(id=status)
                            )
        to_do_list.save()
        return redirect("home page")


class CategoryList(APIView):
    """
    This API Is Created For Category Data GET,POST Opration
    """
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        category = Category.objects.all()
        serializer = CategorySer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = CategorySer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    This API  Is Created For Get Particular One Category GET,PUT,DELETE Opration
    """
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        category = self.get_object(pk)
        serializer = CategorySer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        category = self.get_object(pk)
        serializer = CategorySer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        category = self.get_object(pk=pk)
        category.delete()
        msg = {"massage":"data delete sucessfuly"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)


class TodoList(APIView):
    """
    This API Is Created For To Do List Data GET,POST Opration
    """
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        to_do_list = To_Do_List.objects.all()
        serializer = To_Do_ListSer(to_do_list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = To_Do_ListSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TodolistDetail(APIView):
    """
    This API  Is Created For Get Particular One To Do List  GET,PUT,DELETE Opration
    """
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return To_Do_List.objects.get(pk=pk)
        except To_Do_List.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        to_do_list = self.get_object(pk)
        serializer = To_Do_ListSer(to_do_list)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk,format=None):
        to_do_list = self.get_object(pk)
        serializer = To_Do_ListSer(to_do_list,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        to_do_list = self.get_object(pk=pk)
        to_do_list.delete()
        msg = {"massage":"data delete sucessfuly"}
        return Response(msg,status=status.HTTP_204_NO_CONTENT)