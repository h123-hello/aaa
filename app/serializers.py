from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer

from app.models import User, Employee


def validate(attrs):
    username = attrs.get("username")
    user = User.objects.filter(username=username).first()
    if user:
        raise exceptions.ValidationError("用户名已存在")
    return attrs


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 3,
                "error_messages": {
                    "required": "用户名没有",
                    "min_length": "用户名长度不够"
                }
            }
        }

class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        # fields = "__all__"

        fields = ("id", "emp_name", "img", "salary", "age", "age_name",)
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 3,
                "error_messages": {
                    "required": "用户名没有",
                    "min_length": "用户名长度不够"
                }
            }
        }