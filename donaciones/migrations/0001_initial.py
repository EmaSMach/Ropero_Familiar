import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('clothes', models.DecimalField(decimal_places=3, max_digits=4)),
                ('shoes', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4)])),
                ('accesories', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(4)])),
                ('ticket_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('dni', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(8)])),
                ('birth', models.DateField(null=True)),
                ('role', models.CharField(choices=[('r', 'Referente'), ('f', 'Familiar')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Referring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(15)])),
                ('adress', models.CharField(max_length=80)),
                ('last_buy', models.DateTimeField(null=True)),
                ('family_last_buy', models.CharField(max_length=65, null=True)),
                ('family', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='donaciones.Family')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referentes', to='donaciones.Neighborhood')),
            ],
        ),
    ]
