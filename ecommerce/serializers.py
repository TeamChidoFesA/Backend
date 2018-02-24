from rest_framework import serializers
from ecommerce import models


class SignUpSerializer(serializers.Serializer):

    mail = serializers.EmailField()

    password = serializers.CharField()

    token = serializers.CharField()

    def create(self, data):

        models.User.objects.create(**data)

    class Meta:
        model = models.User

        fields = (
            'mail',
            'password',
            'token'
        )

        read_only_fields = (
            'type_user'
        )

class CatAttributeSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    attribute = serializers.CharField()
    
    class Meta:
        model = models.Cat_attribute

        fields = (
            'id',
            'attribute'
        )
