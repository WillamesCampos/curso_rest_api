# Generated by Django 3.0.4 on 2020-06-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_atracao_foto'),
        ('ponto_turistico', '0012_auto_20200627_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='atracoes',
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
