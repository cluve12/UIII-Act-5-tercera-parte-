from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    direccion = models.CharField(max_length=100)
    foto_sucursal = models.ImageField(upload_to='sucursales/fotos/', null=True, blank=True)  # NUEVO CAMPO
    
    def __str__(self):
        return self.nombre

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="clientes")
    foto_perfil = models.ImageField(upload_to='clientes_fotos/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="empleados")
    nombre = models.CharField(max_length=100, default="Empleado")
    telefono = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()
    puesto = models.CharField(max_length=50)
    foto_perfil = models.ImageField(upload_to='empleados/fotos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.puesto} - {self.sucursal.nombre}"