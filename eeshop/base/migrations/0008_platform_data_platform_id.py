# Generated by Django 4.1.3 on 2022-11-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_platform_data_platform_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform_data',
            name='platform_id',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
