from django.contrib import admin

from .models import Contato


# Register your models here.
@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'assunto', 'telefone', 'mensagem', 'data_envio')
    search_fields = ('nome', 'email')
    list_filter = ('data_envio',)
    ordering = ('-data_envio',)