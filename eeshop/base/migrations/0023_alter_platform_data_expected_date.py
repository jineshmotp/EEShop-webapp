# Generated by Django 4.1.3 on 2022-12-20 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_platform_data_expected_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform_data',
            name='expected_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 11, 12, 41, 145459)),
        ),
    ]
