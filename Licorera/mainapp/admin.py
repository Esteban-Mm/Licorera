from django.contrib import admin
from .models import Producto, Venta

# Register your models here.
admin.site.register(Producto)
admin.site.register(Venta)

titulo = "Licorera Pascualina"
suptitulo = "Panel de gestion"

admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = suptitulo