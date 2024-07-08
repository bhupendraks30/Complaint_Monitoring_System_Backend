
from rest_framework import serializers
from .models import *

# class ComplaintSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Complaint
#         fields = '__all__'
#         read_only_fields = ('status',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'mobile_number', 'gender', 'state', 'district', 'city', 'address', 'pin_code', 'password', 'image', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'image': {'required': False, 'allow_null': True},
        }



class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ('status',)

 