from django.contrib import admin
from .models import *


"""faz o registro dos planos"""
@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'qtd_max_telas')


"""faz o registro dos filmes"""
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'diretor', 'genero','duracao', 'modificado', 'ativo')


"""faz o registros das series"""
@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'diretor', 'qtd_temporadas', 'qtd_episodios')

    
