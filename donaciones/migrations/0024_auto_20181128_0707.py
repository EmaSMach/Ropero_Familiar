# Generated by Django 2.1.1 on 2018-11-28 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0023_auto_20181128_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyentry',
            name='last_entry',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
