from dataclasses import field
from rest_framework import serializers
from .models import *


class CategorySer(serializers.ModelSerializer):
    """
    This Serializer Is Created For Category API
    """
    class Meta:
        model = Category
        fields = "__all__"
        depth = 1
    

class To_Do_ListSer(serializers.ModelSerializer):
    """
    This Serializer Is Creaded For To Do List API
    """
    class Meta:
        model = To_Do_List
        fields = "__all__"
        depth = 1  