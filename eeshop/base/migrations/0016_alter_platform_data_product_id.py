# Generated by Django 4.1.3 on 2022-12-16 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_platform_data_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform_data',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
    ]
