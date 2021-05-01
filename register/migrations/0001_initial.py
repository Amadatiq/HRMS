# Generated by Django 3.1.2 on 2020-10-11 12:26

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family', models.IntegerField()),
                ('doj', models.DateField(default=datetime.datetime(2020, 10, 11, 12, 26, 14, 615743, tzinfo=utc), verbose_name='Date')),
                ('exp', models.IntegerField()),
                ('phone', models.CharField(max_length=14)),
                ('address', models.TextField()),
                ('cv', models.FileField(null=True, upload_to='pics')),
                ('dept', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='register.department')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ltype', models.CharField(choices=[('Annual', 'Annual'), ('Sick', 'Sick')], default=1, max_length=100)),
                ('from_date', models.DateField(default=datetime.date.today)),
                ('to_date', models.DateField(default=datetime.date.today)),
                ('reason', models.TextField(default='Not Feeling Well', max_length=1200)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='register.employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='register.position'),
        ),
    ]