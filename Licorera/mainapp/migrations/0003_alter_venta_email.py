# Generated by Django 4.0.4 on 2022-05-23 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo'),
        ),
    ]
