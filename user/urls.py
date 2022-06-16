from django.urls import path
from .views import UserList,UserDetail
from .views import login,Register,user_signin


urlpatterns = [
    path('',login,name="login"),
    path('signup/',user_signin),
    path('register/',Register.as_view(),name="register page"),
    path('user/', UserList.as_view(),name="user data"),
    path('user/<int:pk>/', UserDetail.as_view(),name="user data one"),
]