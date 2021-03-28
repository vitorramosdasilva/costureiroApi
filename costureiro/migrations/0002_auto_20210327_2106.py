# Generated by Django 3.1.7 on 2021-03-27 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costureiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendaservico',
            options={'verbose_name_plural': 'agenda servicos'},
        ),
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'verbose_name_plural': 'avaliacoes'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='formapagamento',
            options={'verbose_name_plural': 'forma pagamentos'},
        ),
        migrations.AlterModelOptions(
            name='habilidade',
            options={'verbose_name_plural': 'habilidades'},
        ),
        migrations.AlterModelOptions(
            name='prestador',
            options={'verbose_name_plural': 'prestadores'},
        ),
        migrations.AlterModelOptions(
            name='statusservico',
            options={'verbose_name_plural': 'status servicos'},
        ),
        migrations.AlterModelOptions(
            name='tipoprestador',
            options={'verbose_name_plural': 'tipo prestadores'},
        ),
        migrations.AlterModelTable(
            name='avaliacao',
            table='tb_avaliacao',
        ),
    ]
