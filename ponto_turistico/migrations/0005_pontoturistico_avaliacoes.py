# Generated by Django 3.0.4 on 2020-04-02 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('ponto_turistico', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
