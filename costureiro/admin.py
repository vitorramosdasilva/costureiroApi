from django.contrib import admin
from .models import (
    Habilidade,
    FormaPagamento,
    TipoPrestador,
    Prestador,
    Cliente,
    StatusServico,
    AgendaServico,
    Avaliacao
)

admin.site.register(Habilidade)
admin.site.register(FormaPagamento)
admin.site.register(TipoPrestador)


admin.site.register(Prestador)
admin.site.register(Cliente)
admin.site.register(StatusServico)
admin.site.register(AgendaServico)
admin.site.register(Avaliacao)

