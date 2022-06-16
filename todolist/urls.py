from django.urls import path
from .views import (TodoList,TodolistDetail,CategoryList,CategoryDetail,
                    Home_page,UserUpdate,DeleteTodolist,AddToDoList)


urlpatterns = [
    path('home/',Home_page.as_view(),name="home page"),
    path("updatetodo/<int:pk>/",UserUpdate.as_view(),name="update to do list"),
    path("addlist/",AddToDoList.as_view()),
    path("delete/<int:pk>",DeleteTodolist.as_view()),
    path('todolistdata/', TodoList.as_view(),name="To Do List Data"),
    path('todolistdata/<int:pk>/', TodolistDetail.as_view(),name="To Do List Data One"),
    path('categorydata/', CategoryList.as_view(),name="Category Data"),
    path('categorydata/<int:pk>/', CategoryDetail.as_view(),name="Category Data One"),
]