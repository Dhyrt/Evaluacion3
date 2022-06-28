from itertools import product
from tkinter import CASCADE
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    id_tipo_prod = models.IntegerField(null=False, primary_key=True)
    tipo_prod = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_prod
    
    class Meta:
        db_table = 'db_tipoProducto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom_prod
    
    class Meta:
        db_table = 'db_producto'

opciones_consultas = [
    [0, "Puente Alto"],
    [1, "La Florida"],
    [2, "La Pintana"],
    [3, "San Bernardo"],
]

class Comuna(models.Model):
    cod_comuna = models.IntegerField(null=False, primary_key=True)
    nom_comuna = models.CharField(max_length=150)

    def __str__(self):
        return self.nom_comuna

    class Meta:
        db_table = 'db_comuna'

class Cliente(models.Model):
    id_cli = models.IntegerField(null=False, primary_key=True)
    nom_cli = models.CharField(max_length=150)
    ap_cli = models.CharField(max_length=150)
    run_cli = models.CharField(max_length=9) #Cambio del run por num a char para hacer la restriccion por largo
    fono = models.CharField(max_length=13)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, choices=opciones_consultas)
    direccion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    foto = models.ImageField(null=True)

    def __str__(self):
        return self.nom_cli

    class Meta:
        db_table = 'db_cliente'

class Suscripcion(models.Model):
    user = models.CharField(primary_key=True, max_length=50)
    suscripcion = models.BooleanField(null=True)

    def __str__(self):
        return str(self.suscripcion)

    class Meta:
        db_table = 'db_sus'

class Estado(models.Model):
    id_estado = models.IntegerField(null=False, primary_key=True)
    estado_compra = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_compra

    class Meta:
        db_table = 'db_estado_comp'

class carro():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar_prod(self, producto):
        codigo = str(producto.codigo)
        if codigo not in self.carrito.keys():
            self.carrito[codigo] = {
                "codigo" : producto.codigo,
                "nombre" : producto.nombre,
                "cant" : 1,
                "precio" : producto.precio,
                "stock" : producto.stock,
                "img" : producto.img.url,
            }
        else:
            self.carrito[codigo]["cant"] += 1
            self.carrito[codigo]["precio"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def sumar(self, producto):
        codigo = str(producto.codigo)
        if codigo in self.carrito.keys():
            self.carrito[codigo]["cant"] += 1
            self.carrito[codigo]["precio"] += producto.precio
            self.guardar_carrito()
    
    def eliminar(self, producto):
        codigo = str(producto.codigo)
        if codigo in self.carrito:
            del self.carrito[codigo]
            self.guardar_carrito()

    def restar(self, producto):
        codigo = str(producto.codigo)
        if codigo in self.carrito.keys():
            self.carrito[codigo]["cant"] -= 1
            self.carrito[codigo]["precio"] -= producto.precio
            if self.carrito[codigo]["cant"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

class Compra(models.Model):
    cod_compra = models.BigIntegerField(null=False, primary_key=True)
    nom_prod = models.CharField(max_length=50)
    cod_prod = models.IntegerField()
    img = models.ImageField(upload_to="carro", null=True)
    cant = models.IntegerField()
    total = models.IntegerField()
    estado_compra = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cod_compra

    class Meta:
        db_table = 'db_compra'

class listaDeseado(models.Model):
    nom = models.CharField(max_length=50)
    cod = models.IntegerField()
    prec = models.IntegerField()
    sto = models.IntegerField()
    imag = models.ImageField(upload_to="listaDeseos", null=True)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = 'db_listaDeseos'

class TipoUsuario(models.Model):
    id_tipo_us = models.IntegerField(null=False, primary_key=True)
    tipo_usuario = models.CharField(max_length=150)
    
    def __str__(self):
        return self.tipo_usuario

    class Meta:
        db_table = 'db_tipoUsuario'

class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False, primary_key=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nom_usuario = models.CharField(max_length=50)
    ap_usuario = models.CharField(max_length=150)
    run_usuario = models.IntegerField()
    dv_usuario = models.CharField(max_length=1)
    fono = models.CharField(max_length=13)
    
    def __str__(self):
        return self.nom_usuario

    class Meta:
        db_table = 'db_usuarios'