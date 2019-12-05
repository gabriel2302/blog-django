from django.contrib import admin
from .models import Categoria

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):

    #responsável por exibir os valores dos campos na área administrativa
    list_display = ('id', 'nome_cat')

    #links para edição no admin
    list_display_links = ('id', 'nome_cat')

admin.site.register(Categoria, CategoriaAdmin)