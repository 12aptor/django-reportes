# Generated by Django 4.1.6 on 2023-02-11 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventamodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]