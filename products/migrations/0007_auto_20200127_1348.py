# Generated by Django 2.2 on 2020-01-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200127_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]