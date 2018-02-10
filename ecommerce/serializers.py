from rest_framework import serializers
from . import models


class SignUpSerializer(serializers.Serializer):

    mail = serializers.EmailField()

    password = serializers.CharField()

    token = serializers.CharField()

    class Meta:
        model = models.User

        fields = (
            'mail',
            'password',
            'token'
        )

    