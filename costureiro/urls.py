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

# urlpatterns = [

# path('habilidades/', HabilidadesApiViews.as_view(), name='habilidades'),
# path('habilidades/<int:pk>/', HabilidadesApiViews.as_view(), name='habilidade'),
# path('formaPagamentos/', FormaPagamentosAPIView.as_view(), name='forma_pagamentos'),
# path('formaPagamentos/<int:pk>/', FormaPagamentoAPIView.as_view(), name='forma_pagamento'),
# path('tipoPrestadores/', TipoPrestadoresAPIView.as_view(), name='tipo_prestadores'),
# path('tipoPrestadores/<int:pk>/', TipoPrestadorAPIView.as_view(), name='forma_pagamento'),
# path('prestadores/', PrestadoresAPIView.as_view(), name='prestadores'),
# path('prestadores/<int:pk>/', PrestadorAPIView.as_view(), name='prestador'),
# path('clientes/', ClientesAPIView.as_view(), name='clientes'),
# path('clientes/<int:pk>/', ClienteAPIView.as_view(), name='cliente'),
# path('statusServicos/', StatusServicosAPIView.as_view(), name='status_servicos'),
# path('statusServicos/<int:pk>/', StatusServicoAPIView.as_view(), name='status_servico'),
# path('agendaServicos/', AgendaServicosAPIView.as_view(), name='agenda_servicos'),
# path('agendaServicos/<int:pk>/', AgendaServicoAPIView.as_view(), name='agenda_servico'),

# ]

