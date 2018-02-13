from django.db import models
from ecommerce.models.user import (
    User,
    Seller,
    Direction
)
from ecommerce.models.catalog import (
    Cat_category,
    Cat_status_order,
    Cat_type_pay
)

class Product(models.Model):

    seller =  models.ForeignKey(
        Seller, on_delete=models.CASCADE, null=False
    )

    category = models.ForeignKey(
        Cat_category,
        on_delete=models.CASCADE
    )   

    titulo = models.CharField(
        max_length=255, null=False
    )

    descripcion = models.TextField()
    
    cantidad = models.CharField(
        max_length=255, null=False
    )

    precio = models.FloatField(
        null=False, default=None
    )

    stock = models.PositiveIntegerField(
        null=False
    )

    pedido = models.BooleanField(
        default=False
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Product"   

    def __str__(self):
        return self.titulo+' ('+self.precio+')'


class Wishes(models.Model):

    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Wishes"  

    def __str__(self):
        return self.product.titulo


class Favorites(models.Model):
    
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Favorites"  

    def __str__(self):
        return self.product.titulo           
  

class Review(models.Model):
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    resena = models.TextField()

    calificacion = models.PositiveIntegerField()

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Review"

    def __str__(self):
        return self.resena       


class Observation(models.Model):

    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    observacion = models.TextField()
    
    calificacion = models.PositiveIntegerField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Observation" 

    def __str__(self):
        return self.observacion                 


class Request(models.Model):
    
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    peticion = models.TextField()
    
    respuesta = models.TextField()
    
    num_peticion = models.PositiveIntegerField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Request"

    def __str__(self):
        return self.peticion
     

class Message(models.Model):
    
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    mensaje = models.TextField()
    
    atendido = models.BooleanField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Message"

    def __str__(self):
        return self.mensaje


class Order(models.Model):

    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    direction =  models.ForeignKey(
        Direction, on_delete=models.CASCADE
    )

    """
    This is useless

    factura =  models.ForeignKey(
        Direction, on_delete=models.CASCADE, related_name="facturas"
    )
    """

    status = models.ForeignKey(
        Cat_status_order, on_delete=models.CASCADE
    )

    total = models.FloatField(
        null=False, blank=True, default=None
    )

    fecha = models.DateTimeField()

    tipo_pago = models.ForeignKey(
        Cat_type_pay, on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Order" 

    def __str__(self):
        return self.total


class Reports(models.Model):

    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    reporte = models.TextField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Reports"

    def __str__(self):
        return self.observacion             
