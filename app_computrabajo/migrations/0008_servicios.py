# Generated by Django 4.0.1 on 2022-03-19 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_computrabajo', '0007_empleos_ciudad_empleos_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
    ]