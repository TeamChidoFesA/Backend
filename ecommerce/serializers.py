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

class CatCategorySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    category = serializers.CharField()

    class Meta:
        fields = (
            'id',
            'category'
        )


class CatPayTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    pay_type = serializers.CharField()

    class Meta:
        field = (
            'id',
            'pay_type'
        )


class CatSkillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill = serializers.CharField()

    class Meta:
        field = (
            'id',
            'skill'
        )


class CatStatusOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        field = (
            'id',
            'status',
            'description'
        )


class CatTypeUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type_user = serializers.CharField()

    class Meta:
        field = (
            'id',
            'type_user'
        ) 
