from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal, Cliente, Empleado

# ==========================================
# FUNCIÓN PRINCIPAL - PÁGINA DE INICIO
# ==========================================
def inicio_subway(request):
    return render(request, 'app_Subway/inicio.html')

# ==========================================
# FUNCIONES PARA SUCURSALES
# ==========================================
def agregar_sucursal(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        horario_apertura = request.POST['horario_apertura']
        horario_cierre = request.POST['horario_cierre']
        direccion = request.POST['direccion']
        
        sucursal = Sucursal(
            nombre=nombre,
            telefono=telefono,
            horario_apertura=horario_apertura,
            horario_cierre=horario_cierre,
            direccion=direccion
        )
        
        if 'foto_sucursal' in request.FILES:
            sucursal.foto_sucursal = request.FILES['foto_sucursal']
        
        sucursal.save()
        return redirect('ver_sucursales')
    
    return render(request, 'app_Subway/sucursal/agregar_sucursal.html')

def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'app_Subway/sucursal/ver_sucursales.html', {'sucursales': sucursales})

def detalle_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    clientes = sucursal.clientes.all()
    empleados = sucursal.empleados.all()
    
    return render(request, 'app_Subway/sucursal/detalle_sucursal.html', {
        'sucursal': sucursal,
        'clientes': clientes,
        'empleados': empleados
    })

def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    return render(request, 'app_Subway/sucursal/actualizar_sucursal.html', {'sucursal': sucursal})

def realizar_actualizacion_sucursal(request, id):
    if request.method == 'POST':
        sucursal = get_object_or_404(Sucursal, id=id)
        sucursal.nombre = request.POST['nombre']
        sucursal.telefono = request.POST['telefono']
        sucursal.horario_apertura = request.POST['horario_apertura']
        sucursal.horario_cierre = request.POST['horario_cierre']
        sucursal.direccion = request.POST['direccion']
        
        if 'foto_sucursal' in request.FILES:
            sucursal.foto_sucursal = request.FILES['foto_sucursal']
        
        sucursal.save()
        return redirect('ver_sucursales')
    
    return redirect('ver_sucursales')

def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('ver_sucursales')
    
    return render(request, 'app_Subway/sucursal/borrar_sucursal.html', {'sucursal': sucursal})

# ==========================================
# FUNCIONES PARA EMPLEADOS
# ==========================================
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'app_Subway/empleados/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        sucursal_id = request.POST['sucursal']
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        salario = request.POST['salario']
        fecha_contratacion = request.POST['fecha_contratacion']
        puesto = request.POST['puesto']
        
        sucursal = get_object_or_404(Sucursal, id=sucursal_id)
        
        empleado = Empleado(
            sucursal=sucursal,
            nombre=nombre,
            telefono=telefono,
            salario=salario,
            fecha_contratacion=fecha_contratacion,
            puesto=puesto
        )
        
        if 'foto_perfil' in request.FILES:
            empleado.foto_perfil = request.FILES['foto_perfil']
        
        empleado.save()
        return redirect('ver_empleados')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'app_Subway/empleados/agregar_empleado.html', {'sucursales': sucursales})

def actualizar_foto_perfil(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if request.method == 'POST':
        if 'foto_perfil' in request.FILES:
            empleado.foto_perfil = request.FILES['foto_perfil']
            empleado.save()
            return redirect('ver_empleados')
    
    return render(request, 'app_Subway/empleados/actualizar_foto_perfil.html', {'empleado': empleado})

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.telefono = request.POST['telefono']
        empleado.salario = request.POST['salario']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.puesto = request.POST['puesto']
        empleado.sucursal = get_object_or_404(Sucursal, id=request.POST['sucursal'])
        empleado.save()
        return redirect('ver_empleados')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'app_Subway/empleados/actualizar_empleado.html', {
        'empleado': empleado,
        'sucursales': sucursales
    })

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    
    return render(request, 'app_Subway/empleados/borrar_empleado.html', {'empleado': empleado})

# ==========================================
# FUNCIONES PARA CLIENTES
# ==========================================
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_Subway/clientes/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        fecha_registro = request.POST['fecha_registro']
        sucursal_id = request.POST['sucursal']
        
        sucursal = get_object_or_404(Sucursal, id=sucursal_id)
        
        cliente = Cliente(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            fecha_registro=fecha_registro,
            sucursal=sucursal
        )
        
        if 'foto_perfil' in request.FILES:
            cliente.foto_perfil = request.FILES['foto_perfil']
        
        cliente.save()
        return redirect('ver_clientes')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'app_Subway/clientes/agregar_cliente.html', {'sucursales': sucursales})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.direccion = request.POST['direccion']
        cliente.telefono = request.POST['telefono']
        cliente.correo = request.POST['correo']
        cliente.fecha_registro = request.POST['fecha_registro']
        cliente.sucursal = get_object_or_404(Sucursal, id=request.POST['sucursal'])
        
        if 'foto_perfil' in request.FILES:
            cliente.foto_perfil = request.FILES['foto_perfil']
        
        cliente.save()
        return redirect('ver_clientes')
    
    sucursales = Sucursal.objects.all()
    return render(request, 'app_Subway/clientes/actualizar_cliente.html', {
        'cliente': cliente,
        'sucursales': sucursales
    })

def actualizar_foto_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        if 'foto_perfil' in request.FILES:
            cliente.foto_perfil = request.FILES['foto_perfil']
            cliente.save()
            return redirect('ver_clientes')
    
    return render(request, 'app_Subway/clientes/actualizar_foto_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    
    return render(request, 'app_Subway/clientes/borrar_cliente.html', {'cliente': cliente})