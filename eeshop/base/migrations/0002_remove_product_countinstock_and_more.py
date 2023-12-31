# Generated by Django 4.1.3 on 2022-11-11 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='countInStock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='numReviews',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.CreateModel(
            name='Platform_data',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('platform_id', models.IntegerField(blank=True, default=1, null=True)),
                ('platform_name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('countInStock', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('expected_date', models.DateTimeField(auto_now_add=True)),
                ('website_link', models.TextField(blank=True, null=True)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
