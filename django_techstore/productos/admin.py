from django.contrib import admin

from .models import Factura, DetalleFactura

from .models import Producto, Categoria

admin.site.register(Producto)
admin.site.register(Categoria)

# Register your models here.


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'usuario', 'fecha_hora', 'total')
    readonly_fields = ('numero', 'fecha')       # sigue mostrando la fecha original como campo de solo lectura
    date_hierarchy = 'fecha'                    # añade navegación por fecha si lo deseas

    def fecha_hora(self, obj):
        return obj.fecha.strftime("%d/%m/%Y %H:%M:%S")
    fecha_hora.short_description = 'Fecha y hora'


@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad', 'subtotal')