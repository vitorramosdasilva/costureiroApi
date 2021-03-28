from . import models
from rest_framework import fields, serializers
from costureiro.models import DIAS_TRABALHO_CHOICES, HORARIO_TRABALHO_CHOICES


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Habilidade
        fields = '__all__'


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormaPagamento
        fields = '__all__'


class TipoPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoPrestador
        fields = '__all__'


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prestador
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'


class StatusServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatusServico
        fields = '__all__'


class AgendaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AgendaServico
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Avaliacao
        fields = '__all__'


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    dias_trabalho = fields.MultipleChoiceField(choices=DIAS_TRABALHO_CHOICES)
    horario_trabalho = fields.MultipleChoiceField(choices=HORARIO_TRABALHO_CHOICES)

