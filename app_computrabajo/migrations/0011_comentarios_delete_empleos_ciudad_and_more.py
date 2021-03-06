# Generated by Django 4.0.1 on 2022-03-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_computrabajo', '0010_remove_servicios_subtitulo_orienta_subtitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Empleos_Ciudad',
        ),
        migrations.DeleteModel(
            name='Empleos_Estado_Federal',
        ),
        migrations.DeleteModel(
            name='Empleos_Localizacion',
        ),
        migrations.DeleteModel(
            name='Empleos_Sueldo',
        ),
    ]
