# Generated by Django 2.1.1 on 2018-11-30 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0026_auto_20181129_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesdonation',
            name='quantity_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(0)], verbose_name='Cantidad Total'),
        ),
    ]
