# Generated by Django 4.1.2 on 2022-12-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'reserva',
                'verbose_name_plural': 'reservas',
            },
        ),
    ]
