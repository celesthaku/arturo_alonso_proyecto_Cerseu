# Generated by Django 4.2.1 on 2023-06-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0004_alter_platos_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='Perú', max_length=40),
        ),
    ]
