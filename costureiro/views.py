from rest_framework import generics, viewsets
from .models import *
from .serializers import *

"""
API V1
"""


class HabilidadesViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class FormaPagamentosViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer


class TipoPrestadoresViewSet(viewsets.ModelViewSet):
    queryset = TipoPrestador.objects.all()
    serializer_class = TipoPrestadorSerializer


class PrestadoresViewSet(viewsets.ModelViewSet):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class StatusServicosViewSet(viewsets.ModelViewSet):
    queryset = StatusServico.objects.all()
    serializer_class = StatusServicoSerializer


class StatusServicoViewSet(viewsets.ModelViewSet):
    queryset = StatusServico.objects.all()
    serializer_class = StatusServicoSerializer


class AgendaServicosViewSet(viewsets.ModelViewSet):
    queryset = AgendaServico.objects.all()
    serializer_class = AgendaServicoSerializer


class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer



