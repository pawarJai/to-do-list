from statistics import mode
from django.db import models
from user.models import User

# Create your models here.

class Status(models.Model):
    """
    This Model Is Created for Status
    """
    label = models.CharField(max_length=250)

    def __str__(self):
        return self.label

class Category(models.Model):
    """
    This Model Is Created For To Do List Category
    """
    label = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

class To_Do_List(models.Model):
    """
    This Model Is Created For Create To Do List
    """
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return self.title



