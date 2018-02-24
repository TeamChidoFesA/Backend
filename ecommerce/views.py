from django.http import HttpResponse, JsonResponse
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
        print(cat_attributes)
        return JsonResponse(serializer.data, safe=False)
