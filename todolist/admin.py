from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","label","created_at"]

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["id","label"]

@admin.register(To_Do_List)
class To_Do_ListAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","category","user","date","created_at","status"]

