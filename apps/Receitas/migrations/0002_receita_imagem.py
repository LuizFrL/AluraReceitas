# Generated by Django 3.0.7 on 2020-06-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
