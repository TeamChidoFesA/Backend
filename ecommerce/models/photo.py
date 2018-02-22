from django.db import models
from ecommerce.models.user import Seller
from ecommerce.models.content import Product

class Photo_seller(models.Model):

    seller =  models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to = 'sellers/'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "PhotoSeller" 

    def __str__(self):
        return self.foto        
             

class Photo_prod(models.Model):

    producto =  models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to = 'sellers/'
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "PhotoProduct" 

    def __str__(self):
        return self.foto 