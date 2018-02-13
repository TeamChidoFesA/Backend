from django.db import models
from ecommerce.models.user import Seller
from ecommerce.models.content import (
    Product,
    Order
)
from ecommerce.models.catalog import (
    Cat_attribute,
    Cat_skill
)


class Rel_ord_pro(models.Model):

    order =  models.ForeignKey(
        Order, on_delete=models.CASCADE
    )

    product =  models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    cantidad =  models.PositiveIntegerField()

    class Meta:
        db_table = "RelOrdPro"

    def __str__(self):
        return self.observacion 

class Rel_pro_att(models.Model):

    product =  models.ForeignKey(
        Product, on_delete=models.CASCADE
    )

    attribute =  models.ForeignKey(
        Cat_attribute, on_delete=models.CASCADE
    )

    valor =  models.CharField(max_length=255)

    class Meta:
        db_table = "RelProAtt"

    def __str__(self):
        return self.observacion 

class Rel_sel_ski(models.Model):

    seller =  models.ForeignKey(
        Seller, on_delete=models.CASCADE
    )

    skill =  models.ForeignKey(
        Cat_skill, on_delete=models.CASCADE
    )

    class Meta:
        db_table = "RelSelSki"

    def __str__(self):
        return self.observacion 