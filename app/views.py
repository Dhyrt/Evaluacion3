from math import fabs
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from app.models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User, Group

# Create your views here.
def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    if request.method == 'POST':
        carrito = carro()
        carrito.codigo = request.POST.get('prod_codigo')
        carrito.nombre = request.POST.get('prod_nombre')
        carrito.stock = request.POST.get('prod_stock')
        carrito.precio = request.POST.get('prod_precio')
        carrito.img = request.POST.get('prod_img')
        carrito.cant = request.POST.get('prod_cant')
        carrito.save()
    return render(request, 'app/index.html', datos)   

def fundacion(request):
    datos = {
        'suscripcion' : Suscripcion()
    }
    if request.method == 'POST':
        sus = Suscripcion()
        sus.user = request.POST.get('nom_cli')
        sus.suscripcion = request.POST.get('sus')
        sus.save

    return render(request, 'app/fundacion.html' , datos)

def fundacionDes(request):
    if request.method == 'POST':
        sus = Suscripcion()
        sus.user = request.POST.get('nom_cli')
        sus.suscripcion = request.POST.get('desus')
        sus.save
    return redirect(to="fundacion")

@login_required
def configuracion(request):
    data = {
        'form' : DatosPersonalesForm()
    }
    if request.method == 'POST':
        formulario = DatosPersonalesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos guardados correctamente")
    return render(request, 'app/configuracion.html', data)
    
@login_required # es solo para pedir un login
def perfil(request):
    return render(request, 'app/perfil.html')

def arbustos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = carro()
        carrito.codigo = request.POST.get('prod_codigo')
        carrito.nombre = request.POST.get('prod_nombre')
        carrito.stock = request.POST.get('prod_stock')
        carrito.precio = request.POST.get('prod_precio')
        carrito.img = request.POST.get('prod_img')
        carrito.save()
        datos['mensaje'] = 'Producto agregado al carro'
    return render(request, 'app/arbustos.html', datos)

@login_required
def ayuda(request):
    return render(request, 'app/ayuda.html')

@login_required
def compras(request):
    carrito = carro(request)
    datos = {
        'carrito':carrito,
        'cliente': Cliente()
    }
    return render(request, 'app/compras.html', datos)

def flores(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = carro()
        carrito.codigo = request.POST.get('prod_codigo')
        carrito.nombre = request.POST.get('prod_nombre')
        carrito.stock = request.POST.get('prod_stock')
        carrito.precio = request.POST.get('prod_precio')
        carrito.img = request.POST.get('prod_img')
        carrito.save()
        datos['mensaje'] = 'Producto agregado al carro'
    return render(request, 'app/flores.html', datos)

@login_required
def listaDeseos(request):
    whish = listaDeseado.objects.all()
    datos = {
        'listaDeseo' : whish
    }
    if request.method == 'POST':
        carrito = carro()
        carrito.codigo = request.POST.get('prod_codigo')
        carrito.nombre = request.POST.get('prod_nombre')
        carrito.stock = request.POST.get('prod_stock')
        carrito.precio = request.POST.get('prod_precio')
        carrito.img = request.POST.get('prod_img')
        carrito.save()
    return render(request, 'app/listaDeseos.html', datos)

def maceteros(request):
    productos = Producto.objects.all()
    datos = {
        'listaProductos' : productos
    }
    return render(request, 'app/maceteros.html', datos)

@login_required
def rastreo(request):
    return render(request, 'app/rastreo.html')

def tierraDeHojas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = carro()
        carrito.codigo = request.POST.get('prod_codigo')
        carrito.nombre = request.POST.get('prod_nombre')
        carrito.stock = request.POST.get('prod_stock')
        carrito.precio = request.POST.get('prod_precio')
        carrito.img = request.POST.get('prod_img')
        carrito.save()
        datos['mensaje'] = 'Producto agregado al carro'
    return render(request, 'app/tierraDeHojas.html', datos)
    
@permission_required('app.add_producto')
def agregar(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto guardado correctamente'
        else:
            print(formulario.errors.as_data())
    return render(request, 'app/agregar.html', datos)

@permission_required('app.list_producto')
def listarProducto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request, 'app/listarProducto.html', datos)

@permission_required('app.mod_producto')
def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            datos['form'] = formulario
    return render(request, 'app/modificar.html', datos)

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to="listarProducto")

def eliminarCarro(request, codigo):
    carrito = carro.objects.get(codigo=codigo)
    carrito.delete()
    return redirect(to="compras")

def eliminarDeseo(request, cod):
    deseados = listaDeseado.objects.get(cod=cod)
    deseados.delete()
    return redirect(to="listaDeseos")

def detalle(request, codigo):
    prod = Producto.objects.filter(codigo=codigo)
    datos = {
        'listaProducto' : prod
    }
    
    if request.method == 'POST':
        whish = listaDeseado()
        whish.cod = request.POST.get('prod_cod')
        whish.nom = request.POST.get('prod_nom')
        whish.sto = request.POST.get('prod_sto')
        whish.prec = request.POST.get('prod_prec')
        whish.imag = request.POST.get('img')
        whish.save()
        datos['mensaje'] = 'Producto agregado a lista de deseos'
    return render(request, 'app/detalle.html', datos)

def compraExito(request):
    carrito = carro(request)
    carrito.limpiar()
    return render(request, 'app/compraExito.html')

def registro(request):
    data = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            grupo = Group.objects.get(name='cliente')
            users = User.objects.all()
            for u in users:
                grupo.user_set.add(u)
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def agregar_prod(request, producto_codigo):
    carrito = carro(request)
    producto = Producto.objects.get(codigo=producto_codigo)
    carrito.agregar_prod(producto)
    return redirect("compras")

def eliminar(request, producto_codigo):
    carrito = carro(request)
    producto = Producto.objects.get(codigo=producto_codigo)
    carrito.eliminar(producto)
    return redirect(to="compras")

def restar(request, producto_codigo):
    carrito = carro(request)
    producto = Producto.objects.get(codigo=producto_codigo)
    carrito.restar(producto)
    return redirect(to="compras")

def sumar(request, producto_codigo):
    carrito = carro(request)
    producto = Producto.objects.get(codigo=producto_codigo)
    carrito.sumar(producto)
    return redirect(to="compras")

def limpiar(request):
    carrito = carro(request)
    carrito.limpiar()
    return redirect(to="compras")
