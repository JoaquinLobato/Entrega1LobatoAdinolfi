# Generated by Django 4.1.2 on 2022-11-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Negocio', '0002_productos_stock_alter_empleados_id_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='precio_currency',
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
