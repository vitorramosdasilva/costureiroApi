from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


DIAS_TRABALHO_CHOICES = (
        (1, "Domingo"),
        (2, "Segunda-Feira"),
        (3, "Terça-Feira"),
        (4, "Quarta-Feira"),
        (5, "Quinta-Feira"),
        (6, "Sexta-Feira"),
        (7, "Sábado"),
    )


HORARIO_TRABALHO_CHOICES = (
        (1, "00:00"),
        (2, "01:00"),
        (3, "02:00"),
        (4, "03:00"),
        (5, "04:00"),
        (6, "05:00"),
        (7, "06:00"),
        (8, "07:00"),
        (9, "08:00"),
        (10, "09:00"),
        (11, "10:00"),
        (12, "11:00"),
        (13, "12:00"),
        (14, "13:00"),
        (15, "14:00"),
        (16, "15:00"),
        (17, "16:00"),
        (18, "17:00"),
        (19, "18:00"),
        (20, "19:00"),
        (21, "20:00"),
        (22, "21:00"),
        (23, "22:00"),
        (24, "23:00"),
        (25, "24:00")
)


class Base(models.Model):
    creat_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Habilidade(Base):
    descricao = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_habilidade"
        verbose_name_plural = "habilidades"

    def __str__(self):
        return self.descricao


class FormaPagamento(Base):
    descricao = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_forma_pagamento"
        verbose_name_plural = "forma pagamentos"

    def __str__(self):
        return self.descricao


class TipoPrestador(Base):
    descricao = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_tipo_prestador"
        verbose_name_plural = "tipo prestadores"

    def __str__(self):
        return self.descricao


class Prestador(Base):
    nome_completo = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=25, unique=True)
    data_nascimento = models.DateField(max_length=8)
    telefone = models.CharField(max_length=20)
    dias_trabalho = MultiSelectField(choices=DIAS_TRABALHO_CHOICES)
    horario_trabalho = MultiSelectField(choices=HORARIO_TRABALHO_CHOICES)
    habilidade = models.ForeignKey(Habilidade, on_delete=models.PROTECT)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    numero = models.IntegerField()

    tipo_costureiro = models.ForeignKey(TipoPrestador, on_delete=models.PROTECT)
    aceita_plataforma = models.BooleanField(default=True)

    #OneToMany
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_prestador"
        verbose_name_plural = "prestadores"

    def __str__(self):
        return self.nome_completo


class Cliente(Base):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField(max_length=8)
    cep = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20)

    aceita_plataforma = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # author = models.ForeignKey ( User , on_delete=models.PROTECT )
    # email = models.CharField(max_length=70)

    class Meta:
        db_table = "tb_cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nome_completo


class StatusServico(Base):
    descricao = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_status_servico"
        verbose_name_plural = "status servicos"

    def __str__(self):
        return self.descricao


class Avaliacao(Base):
    prestador = models.ForeignKey(Prestador, on_delete=models.PROTECT)
    estrelas = models.IntegerField()
    nome = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    unique_together = [['prestador', 'author']]

    class Meta:
        db_table = "tb_avaliacao"
        verbose_name_plural = "avaliacoes"


class AgendaServico(Base):
    prestador = models.ForeignKey(Prestador, on_delete=models.PROTECT)
    status_servico = models.ForeignKey(StatusServico, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    # cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    # se o prestador quiser contatar o cliente ....
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "tb_agenda_servico"
        verbose_name_plural = "agenda servicos"

    def __str__(self):
        return self.nome