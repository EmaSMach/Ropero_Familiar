# Generated by Django 2.1.1 on 2018-11-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0018_auto_20181127_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='typesproducts',
            name='quantity_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Cantidad Total'),
        ),
    ]
