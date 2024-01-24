from rest_framework import serializers

from .models import *

class UserCreteSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'email','first_name','last_name', 'password']

    def create(self, validated_data):
       return CustomUser.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name', 'password']


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.first_name = validated_data.get('first_name', instance.first_name)
        # instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.email = validated_data.get('email', instance.email)
        # instance.mobile = validated_data.get('mobile', instance.mobile)
        # instance.role = validated_data.get('role', instance.role)
        # instance.save()
        super().update(instance = instance, validated_data= validated_data)
        return instance  


class EmployeeCreateSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField()
    designation_id=serializers.IntegerField()
 

    class Meta:
        model = Employee
        fields = ['user_id','designation_id','company','emp_id']

    # method for creating the user in employee model

    def create(self , validated_data):
        instance = Employee.objects.create(**validated_data)
        return instance


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    # making serializer for Employee model

    class Meta:
        model = Employee
        fields = ['user', 'designation','company']

        # method for creating the user in employee model
        def update(self , instance , validated_data):
            pass












    