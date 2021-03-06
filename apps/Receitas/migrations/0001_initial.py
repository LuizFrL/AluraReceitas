# Generated by Django 3.0.7 on 2020-06-24 19:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=50)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.TextField()),
                ('dia_preparo', models.DateField(blank=True, default=datetime.datetime.now)),
                ('publicar', models.BooleanField(default=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.Pessoas')),
            ],
        ),
    ]
