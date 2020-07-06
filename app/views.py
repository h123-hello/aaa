from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from app import serializers
from app.models import User
from app.serializers import UserModelSerializer, EmployeeModelSerializer
from utils import exceptions
from utils.response import APIResponse
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin

class UserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        # print(request_data)

        return APIResponse(200, True, results=UserModelSerializer(user_obj).data)
        # return APIResponse("ok")

    # def validate(self, attrs):
    #     username = attrs.get("username")
    #     user = User.objects.filter(username=username).first()
    #     if user:
    #         raise exceptions.ValidationError("用户名已存在")
    #     return attrs

    def get(self, request, *args, **kwargs):
        query_params = request.query_params
        print(query_params)
        username = request.query_params("username")
        password = request.query_params("password")
        user = User.objects.filter(username=username, password=password)
        if user:
            data = UserModelSerializer(user).data
            return APIResponse(200, True, results=data)
        return APIResponse(400, False)


# class RegisterView(ViewSet):
#     def check_user(self,request,*args,**kwargs):
#         return APIResponse("ok")
class EemloyeeView(ListModelMixin, GenericAPIView,CreateModelMixin):
    queryset = Eemloyee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        user_list = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=user_list.data)


    def post(self, request, *args, **kwargs):
        # user_list = self.list(request, *args, **kwargs)
        user_obj = self.create(request,*args,**kwargs)
        return APIResponse(200, True, results=user_obj.data)