# Generated by Django 5.0.6 on 2024-07-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='genero',
            field=models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer'), ('niño', 'Niño'), ('niña', 'Niña')], default='hombre', max_length=10),
        ),
    ]