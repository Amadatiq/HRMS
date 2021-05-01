# Generated by Django 3.1.2 on 2020-10-13 20:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20201013_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Annual', max_length=20)),
                ('numbers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='bs',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='fsc',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='matric',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='ms',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='phd',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cnic',
            field=models.CharField(default='', max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Format: 'xxxxxxxxxxxxx' Enter 13 Digits CNIC (Numbers only).", regex='^^.{4}\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cv',
            field=models.FileField(null=True, unique=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='register.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(default=datetime.datetime(2020, 10, 13, 20, 1, 29, 546152, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='', max_length=14, null=True, validators=[django.core.validators.RegexValidator(message="Format: '03XXxxxxxxx'  Enter 14 Digits.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='register.position'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='register.leavetype'),
        ),
    ]
