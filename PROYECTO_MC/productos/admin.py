from django.contrib import admin
from .models import producto
#Username: Project1
#Password: Papi270802
# Register your models here.
class productoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(producto,productoAdmin)