# Generated by Django 4.1.1 on 2022-09-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TattooApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tattoos',
            name='nombre_artista',
            field=models.CharField(default='pedro', max_length=40),
            preserve_default=False,
        ),
    ]
