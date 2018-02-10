from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class SignUpView(APIView):

    serializer_class = serializers.SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()

        return Response()