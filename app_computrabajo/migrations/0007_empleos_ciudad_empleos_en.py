# Generated by Django 4.0.1 on 2022-02-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_computrabajo', '0006_remove_empleos_ciudad_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleos_ciudad',
            name='empleos_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
