# Generated by Django 3.1.2 on 2020-12-23 10:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20201013_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(default=datetime.datetime(2020, 12, 23, 10, 24, 9, 510469, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.CharField(default='', max_length=1200),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
    ]