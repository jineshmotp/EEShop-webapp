# Generated by Django 4.1.3 on 2022-12-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_platform_data_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform_data',
            name='product_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
