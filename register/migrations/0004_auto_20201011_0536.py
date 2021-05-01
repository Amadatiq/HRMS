# Generated by Django 3.1.2 on 2020-10-11 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20201011_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='user',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='ltype',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(default=datetime.datetime(2020, 10, 11, 12, 36, 24, 631214, tzinfo=utc), verbose_name='Date'),
        ),
    ]