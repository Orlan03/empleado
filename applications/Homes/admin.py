from django.contrib import admin
from .models import Prueba
# Register your models here.


class homeAdmin(admin.ModelAdmin):
    list_display =(
         'titulo',
            'subtitulo',
            'cantidad',

    )


admin.site.register(Prueba, homeAdmin)