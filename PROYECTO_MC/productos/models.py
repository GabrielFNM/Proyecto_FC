from django.db import models

# Create your models here.
class producto(models.Model):
    title = models.CharField(max_length=200, verbose_name="producto")
    description = models.TextField(verbose_name="descripcion")
    image = models.ImageField( verbose_name="imagen del producto", upload_to="img_productos")
    created = models.DateTimeField(auto_now_add=True,verbose_name="fecha de publicación")
    updated = models.DateTimeField(auto_now=True,  verbose_name="fecha de modificación")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
        ordering = ["-created"]
def __str__(self):
    return self.title
