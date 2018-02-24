from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

class SignUpView(APIView):

    serializer_class = serializers.SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        type_user = models.Cat_type_user.objects.get(id=1)
    
        user = serializer.save(type_user=type_user)
        print(user)

        return Response()

class CatAttributeList(APIView):
    serializer_class = serializers.CatAttributeSerializer

    def get(self, request, *args, **kwargs):
        cat_attributes = models.Cat_attribute.objects.all()
        serializer = serializers.CatAttributeSerializer(cat_attributes, many=True)
        return Response(serializer.data,200)

class CatCategoryList(APIView):
    serializer_class = serializers.CatCategorySerializer

    def get(self, request, *args, **kwargs):
        cat_category = models.Cat_category.objects.all()
        serializer = serializers.CatCategorySerializer(cat_category, many=True)
        return Response(serializer.data,200)

class CatPayTypeList(APIView):
    serializer_class = serializers.CatPayTypeSerializer

    def get(self, request, *args, **kwargs):
        cat_pay_type = models.Cat_pay_type.objects.all()
        serializer = serializers.CatPayTypeSerializer(cat_pay_type, many=True)
        return Response(serializer.data,200)


class CatSkillList(APIView):
    serializer_class = serializers.CatSkillSerializer

    def get(self, request, *args, **kwargs):
        cat_skill = models.Cat_skill.objects.all()
        serializer = serializers.CatSkillSerializer(cat_skill, many=True)
        return Response(serializer.data, 200)


class CatStatusOrderList(APIView):
    serializer_class = serializers.CatStatusOrderSerializer

    def get(self, request, *args, **kwargs):
        cat_status_order = models.Cat_status_order.objects.all()
        serializer = serializers.CatStatusOrderSerializer(
            cat_status_order, many=True)
        return Response(serializer.data, 200)


class CatTypeUserList(APIView):
    serializer_class = serializers.CatTypeUserSerializer

    def get(self, request, *args, **kwargs):
        cat_type_user = models.Cat_type_user.objects.all()
        serializer = serializers.CatTypeUserSerializer(cat_type_user, many=True)
        return Response(serializer.data, 200)
