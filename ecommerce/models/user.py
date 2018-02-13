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

    nombre = models.CharField(
        max_length=100, null=False
    )
    
    ape_paterno = models.CharField(
        max_length=100, null=False
    )

    ape_materno = models.CharField(
        max_length=100, null=False
    )

    direccion = models.TextField(
        null=False
    )

    ciudad = models.CharField(
        max_length=255, null=False
    )

    pais = models.CharField(
        max_length=255, null=False
    )

    cod_postal = models.CharField(
        max_length=10, null=False
    )

    telefono = models.CharField(
        max_length=15, null=False
    )

    empresa = models.CharField(
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

    def __str__(self):
        return self.name+" "+self.ape_paterno+" ("+self.cod_postal+")"


class Seller(models.Model):
    user = models.OneToOneField(User,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        max_length=100, null=False
    )

    ape_paterno = models.CharField(
        max_length=100, null=False
    )

    ape_materno = models.CharField(
        max_length=100, null=False
    )

    descripcion = models.TextField()

    foto_perfil = models.ImageField(
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

    def __str__(self):
        return self.nombre+' '+self.ape_paterno


class No_user(models.Model):
    mail =  models.EmailField(
        max_length=255
    )

    area_interes = models.ForeignKey(
        Cat_category, on_delete=models.CASCADE
    )
  
    class Meta:
        db_table = "NoUser" 