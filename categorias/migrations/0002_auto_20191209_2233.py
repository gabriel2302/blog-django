# Generated by Django 2.0 on 2019-12-10 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
