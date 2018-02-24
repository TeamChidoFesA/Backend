from django.db import models
from ecommerce.models.catalog import (
    Cat_type_user,
    Cat_category
)


class User(models.Model):

    mail = models.EmailField(
        max_length=255, null=False
    )

    password = models.CharField(
        max_length=255, null=False
    ) 

    token = models.CharField(
        max_length=255
    )

    type_user = models.ForeignKey(
        Cat_type_user,
        on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.type_user.type_user
    

class Direction(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False
    )

    name = models.CharField(
        max_length=100, null=False
    )
    
    paternal_last_name = models.CharField(
        max_length=100, null=False
    )

    maternal_last_name = models.CharField(
        max_length=100, null=False
    )

    address = models.TextField(
        null=False
    )

    city = models.CharField(
        max_length=255, null=False
    )

    country = models.CharField(
        max_length=255, null=False
    )

    postal_code = models.CharField(
        max_length=10, null=False
    )

    phone_number = models.CharField(
        max_length=15, null=False
    )

    company = models.CharField(
        max_length=255
    )

    rfc = models.CharField(
        max_length=12
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Direction"


class Seller(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE
    )

    """
    This is useless
    name = models.CharField(
        max_length=100, null=False
    )

    ape_paterno = models.CharField(
        max_length=100, null=False
    )

    ape_materno = models.CharField(
        max_length=100, null=False
    )
    """

    description = models.TextField()

    profile_picture = models.ImageField(
        upload_to = 'profile/', default = 'profile/no-img.jpg'
    )

    rating = models.PositiveIntegerField()

    num_user = models.PositiveIntegerField()

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Seller"


class No_user(models.Model):
    mail =  models.EmailField(
        max_length=255
    )

    interest_area = models.ForeignKey(
        Cat_category, on_delete=models.CASCADE
    )
  
    class Meta:
        db_table = "NoUser" 