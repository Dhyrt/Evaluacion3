from django.urls import path, include
from .views import *
from rest_framework import routers
#se encarga de agregar una ruta al api
router = routers.DefaultRouter()
router.register('Producto', ProductoViewSet)

#localhost:8000/api/Producto
urlpatterns = [
    path('', index ,name = 'index'),
    path('registro/', registro ,name = 'registro'),
    path('fundacion/', fundacion,name = 'fundacion'),
    path('fund/', fundacionDes,name = 'fundacionDes'),
    path('configuracion/', configuracion ,name = 'configuracion'),
    path('arbustos/', arbustos ,name = 'arbustos'),
    path('ayuda/', ayuda ,name = 'ayuda'),
    path('compras/', compras ,name = 'compras'),
    path('flores/', flores ,name = 'flores'),
    path('listaDeseos/', listaDeseos ,name = 'listaDeseos'),
    path('maceteros/', maceteros ,name = 'maceteros'),
    path('perfil/', perfil ,name = 'perfil'),
    path('rastreo/', rastreo ,name = 'rastreo'),
    path('tierraDeHojas/', tierraDeHojas ,name = 'tierraDeHojas'),
    path('agregar/', agregar ,name = 'agregar'),
    path('modificar/<codigo>/', modificar ,name = 'modificar'),
    path('listarProducto/', listarProducto ,name = 'listarProducto'),
    path('eliminarProducto/<codigo>/', eliminarProducto ,name = 'eliminarProducto'),
    path('eliminarDeseo/<cod>/' , eliminarDeseo , name = 'eliminarDeseo'),
    path('detalle/<codigo>/' , detalle , name = 'detalle'),
    path('compraExito/' , compraExito , name = 'compraExito'),
    path('agregar_prod/<int:producto_codigo>/' , agregar_prod , name = 'Add'),
    path('eliminar/<int:producto_codigo>/' , eliminar , name = 'Del'),
    path('restar/<int:producto_codigo>/' , restar , name = 'Sub'),
    path('sumar/<int:producto_codigo>/' , sumar , name = 'Sum'),
    path('api/', include(router.urls)),
]

