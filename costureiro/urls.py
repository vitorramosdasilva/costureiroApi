from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()
router.register('habilidades', HabilidadesViewSet)
router.register('formaPagamentos', FormaPagamentosViewSet)
router.register('tipoPrestadores', TipoPrestadoresViewSet)
router.register('prestadores', PrestadoresViewSet)
router.register('clientes', ClientesViewSet)
router.register('statusServicos', StatusServicosViewSet)
router.register('avaliacoes', AvaliacoesViewSet)
router.register('agendaServicos', AgendaServicosViewSet)


