from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio_subway, name='inicio'),
    path('sucursales/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursales/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursales/detalle/<int:id>/', views.detalle_sucursal, name='detalle_sucursal'),  # NUEVA RUTA
    path('sucursales/actualizar/<int:id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursales/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_sucursal, name='realizar_actualizacion_sucursal'),
    path('sucursales/borrar/<int:id>/', views.borrar_sucursal, name='borrar_sucursal'),
    
    # URLs para Empleados
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/actualizar-foto/<int:id>/', views.actualizar_foto_perfil, name='actualizar_foto_perfil'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # URLs para Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)