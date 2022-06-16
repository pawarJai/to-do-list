from dataclasses import field
from rest_framework import serializers
from .models import User


class UserSer(serializers.ModelSerializer):
    """
    This Serializer Is Created For User API
    """
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
            instance.first_name = validated_data.get("first_name")
            instance.last_name = validated_data.get("last_name")
            instance.phone = validated_data.get("phone")
            instance.is_staff = validated_data.get("is_staff")
            instance.is_active = validated_data.get("is_active")
            instance.save()
        return instance
