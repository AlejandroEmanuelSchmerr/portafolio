# Generated by Django 5.0.6 on 2024-11-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='repositorio',
            field=models.URLField(blank=True, null=True),
        ),
    ]
