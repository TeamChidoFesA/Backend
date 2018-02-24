from django.db import models

class Cat_type_user(models.Model):
    
    type_user = models.CharField(
        max_length=255, null=False
    )

    class Meta:
        db_table = "CatTypeUser"

    def __str__(self):
        return self.type_user

class Cat_category(models.Model):
    
    category = models.CharField(
        max_length=255, null=False
    )    

    class Meta:
        db_table = "CatCategory"

    def __str__(self):
        return self.category

class Cat_skill(models.Model):
    
    skill = models.CharField(
        max_length=255, null=False
    ) 

    class Meta:
        db_table = "CatSkill"

    def __str__(self):
        return self.skill

class Cat_attribute(models.Model):
    
    attribute = models.CharField(
        max_length=255, null=False
    )

    class Meta:
        db_table = "CatAttribute"

    def __str__(self):
        return self.attribute

class Cat_pay_type(models.Model):
    
    pay_type = models.CharField(
        max_length=150, null=False
    )

    class Meta:
        db_table = "CatPayType"

    def __str__(self):
        return self.pay_type

class Cat_status_order(models.Model):
    
    status = models.CharField(
        max_length=255
    )

    description = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = "CatStatusOrder"

    def __str__(self):
        return self.status