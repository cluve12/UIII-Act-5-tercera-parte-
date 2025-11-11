from django.contrib import admin
from .models import Sucursal, Cliente, Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo', 'sucursal', 'foto_perfil_thumbnail']
    list_filter = ['sucursal']
    search_fields = ['nombre', 'correo']
    
    def foto_perfil_thumbnail(self, obj):
        if obj.foto_perfil:
            return f'<img src="{obj.foto_perfil.url}" style="width: 50px; height: 50px; object-fit: cover;" />'
        return "Sin foto"
    foto_perfil_thumbnail.allow_tags = True
    foto_perfil_thumbnail.short_description = 'Foto'

admin.site.register(Sucursal)
admin.site.register(Empleado)