# Generated by Django 3.1.2 on 2020-10-11 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(default=datetime.datetime(2020, 10, 11, 12, 27, 39, 944177, tzinfo=utc), verbose_name='Date'),
        ),
    ]
