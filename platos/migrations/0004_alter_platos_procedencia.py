# Generated by Django 4.2.1 on 2023-06-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0003_platos_procedencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='procedencia',
            field=models.CharField(default='', max_length=40),
        ),
    ]