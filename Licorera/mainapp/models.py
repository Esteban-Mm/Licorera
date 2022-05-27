from django.db import models

# Create your models here.

class Producto(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    type = models.CharField(max_length=20, verbose_name="Tipo de licor")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="producto")
    price = models.CharField(max_length=12, verbose_name="Precio")
    stok = models.IntegerField(verbose_name="Cantidad", default=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creado")
    updated_at =  models.DateTimeField(auto_now_add=True, verbose_name="Fecha de editado")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ['-id']

    def __str__(self):
        return self.title

class Venta(models.Model):
    names = models.CharField(max_length=100, verbose_name="Nombres")
    direction = models.CharField(max_length=100, verbose_name="Direccion")
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=30, verbose_name="Celular")
    unit = models.IntegerField(verbose_name="Unidades compradas", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creado")
    updated_at =  models.DateTimeField(auto_now_add=True, verbose_name="Fecha de editado")

    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
        ordering = ['-id']

    def __str__(self):
        return self.names