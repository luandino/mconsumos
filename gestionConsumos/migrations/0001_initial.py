# Generated by Django 4.0.4 on 2022-06-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=2)),
                ('local', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
