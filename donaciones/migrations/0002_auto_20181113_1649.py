# Generated by Django 2.1.1 on 2018-11-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='dni',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='referring',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
