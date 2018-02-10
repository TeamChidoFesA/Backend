from django.db import models

class Cat_type_user(models.Model):
    type_user = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "CatTypeUser"

    def __str__(self):
        return self.type_user

class Cat_category(models.Model):
    category = models.CharField(max_length=255, null=False)    

    class Meta:
        db_table = "CatCategory"

    def __str__(self):
        return self.category

class Cat_skill(models.Model):
    skill = models.CharField(max_length=255, null=False) 

    class Meta:
        db_table = "CatSkill"

    def __str__(self):
        return self.skill

class Cat_attribute(models.Model):
    attribute = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "CatAttribute"

    def __str__(self):
        return self.attribute

class Cat_type_pay(models.Model):
    tipo_pago = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = "CatTypePay"

    def __str__(self):
        return self.tipo_pago

class Cat_status_order(models.Model):
    status = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "CatStatusOrder"

    def __str__(self):
        return self.status

class User(models.Model):
    mail = models.EmailField(max_length=255, null=False)  
    password = models.CharField(max_length=255, null=False) 
    token = models.CharField(max_length=255) 
    type_user = models.OneToOneField(
        Cat_type_user,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.type_user.type_user       

class Direction(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ape_paterno = models.CharField(max_length=100, null=False)
    ape_materno = models.CharField(max_length=100, null=False)
    direccion = models.TextField(null=False)
    ciudad = models.CharField(max_length=255, null=False)
    pais = models.CharField(max_length=255, null=False)
    cod_postal = models.PositiveIntegerField(null=False)
    telefono = models.PositiveIntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    empresa = models.CharField(max_length=255)
    rfc = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Direction"

    def __str__(self):
        return self.name+" "+self.ape_paterno+" ("+self.cod_postal+")"

class Seller(models.Model):
    id_user = models.OneToOneField(User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre = models.CharField(max_length=100, null=False)
    ape_paterno = models.CharField(max_length=100, null=False)
    ape_materno = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    foto_perfil = models.ImageField(upload_to = 'profile/', default = 'profile/no-img.jpg')
    rating = models.PositiveIntegerField()
    num_user = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Seller"    

    def __str__(self):
        return self.nombre+' '+self.ape_paterno

class Product(models.Model):
    id_seller =  models.ForeignKey(Seller, on_delete=models.CASCADE, null=False)
    id_category = models.OneToOneField(
        Cat_category,
        on_delete=models.CASCADE,
        primary_key=True
    )             
    titulo = models.CharField(max_length=255, null=False)
    descripcion = models.TextField()
    cantidad = models.CharField(max_length=255, null=False)
    precio = models.FloatField(null=False, default=None)
    stock = models.PositiveIntegerField(null=False)
    pedido = models.BooleanField(255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Product"   

    def __str__(self):
        return self.titulo+' ('+self.precio+')'

class Wishes(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Wishes"  

    def __str__(self):
        return self.product.titulo     

class Favorites(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Favorites"  

    def __str__(self):
        return self.product.titulo           

class No_user(models.Model):
    mail =  models.EmailField(max_length=255) 
    area_interes = models.ForeignKey(Cat_category, on_delete=models.CASCADE)
  
    class Meta:
        db_table = "NoUser" 

class Photo_seller(models.Model):
    id_seller =  models.ForeignKey(Seller, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to = 'sellers/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PhotoSeller" 

    def __str__(self):
        return self.foto                     

class Photo_prod(models.Model):
    id_producto =  models.ForeignKey(Product, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to = 'sellers/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "PhotoProduct" 

    def __str__(self):
        return self.foto   

class Review(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    resena = models.TextField()
    calificacion = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Review"

    def __str__(self):
        return self.resena       

class Observation(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    observacion = models.TextField()
    calificacion = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Observation" 

    def __str__(self):
        return self.observacion                 

class Request(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    peticion = models.TextField()
    respuesta = models.TextField()
    num_peticion = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Request"

    def __str__(self):
        return self.peticion     

class Message(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    mensaje = models.TextField()
    atendido = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Message"

    def __str__(self):
        return self.mensaje  

class Order(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_direction =  models.ForeignKey(Direction, on_delete=models.CASCADE)
    factura =  models.ForeignKey(Direction, on_delete=models.CASCADE, related_name="facturas")
    id_status = models.OneToOneField(
    Cat_status_order,
        on_delete=models.CASCADE,
        primary_key=True
    )
    total = models.FloatField(null=False, blank=True, default=None)
    fecha = models.DateTimeField()
    id_tipo_pago = models.OneToOneField(
        Cat_type_pay,
        on_delete=models.CASCADE,
        primary_key=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Order" 

    def __str__(self):
        return self.total   

class Reports(models.Model):
    id_user =  models.ForeignKey(User, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    reporte = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Reports"

    def __str__(self):
        return self.observacion             

class Rel_ord_pro(models.Model):
    id_order =  models.ForeignKey(Order, on_delete=models.CASCADE)
    id_product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad =  models.PositiveIntegerField()

    class Meta:
        db_table = "RelOrdPro"

    def __str__(self):
        return self.observacion 

class Rel_pro_att(models.Model):
    id_product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    id_attribute =  models.ForeignKey(Cat_attribute, on_delete=models.CASCADE)
    valor =  models.CharField(max_length=255)

    class Meta:
        db_table = "RelProAtt"

    def __str__(self):
        return self.observacion 

class Rel_sel_ski(models.Model):
    id_seller =  models.ForeignKey(Seller, on_delete=models.CASCADE)
    id_skill =  models.ForeignKey(Cat_skill, on_delete=models.CASCADE)

    class Meta:
        db_table = "RelSelSki"

    def __str__(self):
        return self.observacion 
				

