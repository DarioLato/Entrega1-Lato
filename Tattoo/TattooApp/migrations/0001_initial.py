# Generated by Django 4.1.1 on 2022-09-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fechadenacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('estilo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tattoos',
            fields=[
                ('id_historia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=40)),
                ('apellido_cliente', models.CharField(max_length=40)),
                ('fecha_tat', models.DateField()),
                ('estilo_tat', models.CharField(max_length=200)),
                ('lugar_tat', models.CharField(max_length=200)),
            ],
        ),
    ]
