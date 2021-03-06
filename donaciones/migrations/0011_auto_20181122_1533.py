# Generated by Django 2.1.1 on 2018-11-22 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0010_merge_20181122_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity_total', models.IntegerField(default=0, verbose_name='Cantidad Total')),
            ],
        ),
        migrations.AlterField(
            model_name='family',
            name='firstname',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='family',
            name='lastname',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='sortproducts',
            name='quantity',
            field=models.IntegerField(verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='sortproducts',
            name='types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='donaciones.TypesProducts', verbose_name='Tipos de Producto'),
        ),
    ]
