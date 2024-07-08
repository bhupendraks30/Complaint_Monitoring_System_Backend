from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
# class UserAdmin(admin.ModelAdmin):
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'gender', 'state', 'district', 'city', 'pin_code' ,'role')
    list_display = ('full_name', 'email', 'mobile_number', 'gender', 'state', 'district', 'city', 'pin_code' ,'role' )
    search_fields = ('full_name', 'email', 'mobile_number','role')


@admin.register(Complaint)
# class UserAdmin(admin.ModelAdmin):
class ComplaintAdmin(admin.ModelAdmin):    
    list_display = ('full_name', 'email', 'mobile_number', 'state', 'district', 'city','address', 'pin_code' , 'description', 'date_submitted', 'category','status','cid')
    search_fields = ('full_name', 'email', 'mobile_number')

 
