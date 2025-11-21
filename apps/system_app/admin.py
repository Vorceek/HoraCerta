from django.contrib import admin
from .models import Barbearia, Barbeiro, Servico, Agendamento

@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'nota')
    search_fields = ('nome', 'endereco')


@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cadeira', 'barbearia')
    search_fields = ('nome',)
    list_filter = ('barbearia',)


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao_minutos', 'preco')
    search_fields = ('nome',)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'barbeiro', 'servico', 'data', 'hora', 'status')
    list_filter = ('status', 'data')
    search_fields = ('cliente__username', 'barbeiro__nome')
