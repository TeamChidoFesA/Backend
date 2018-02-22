from django.db import models
from ecommerce.models.user import (
    User,
    Seller,
    Direction
)
from ecommerce.models.catalog import (
    Cat_category,
    Cat_status_order,
    Cat_pay_type
)
from django_fsm import FSMField


class Product(models.Model):

    seller =  models.ForeignKey(
        Seller, on_delete=models.CASCADE, null=False
    )

    category = models.ForeignKey(
        Cat_category,
        on_delete=models.CASCADE
    )   

    tittle = models.CharField(
        max_length=255, null=False
    )

    description = models.TextField()
    
    quantity = models.PositiveIntegerField()

    price = models.FloatField(
        null=False, default=None
    )

    stock = models.PositiveIntegerField(
        null=False
    )

    order = models.BooleanField(
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
        return self.tittle +' ('+self.price+')'


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
        return self.product.tittle


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
        return self.product.tittle           
  

class Review(models.Model):
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    review = models.TextField()

    qualification = models.PositiveIntegerField()

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Review"

    def __str__(self):
        return self.review       


class Observation(models.Model):

    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    observation = models.TextField()
    
    qualification = models.PositiveIntegerField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Observation" 

    def __str__(self):
        return self.observation                 


class Request(models.Model):
    
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    petition = models.TextField()
    
    answer = models.TextField()
    
    num_petition = models.PositiveIntegerField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Request"

    def __str__(self):
        return self.petition
     

class Message(models.Model):
    
    user =  models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    message = models.TextField()
    
    viewed = models.BooleanField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Message"

    def __str__(self):
        return self.message


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

    status = FSMField(
        max_length=50, default=''
    )

    total = models.FloatField(
        null=False, blank=True, default=None
    )

    order_date = models.DateTimeField()

    pay_type = models.ForeignKey(
        Cat_pay_type, on_delete=models.CASCADE
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

    report = models.TextField()
    
    created = models.DateTimeField(
        auto_now_add=True
    )
    
    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "Reports"

    def __str__(self):
        return self.report             
