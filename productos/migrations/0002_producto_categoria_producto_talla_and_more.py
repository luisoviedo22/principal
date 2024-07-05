# Generated by Django 5.0.6 on 2024-07-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default='prenda', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.CharField(default='Null', max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
