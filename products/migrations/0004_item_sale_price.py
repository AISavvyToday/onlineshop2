# Generated by Django 2.2 on 2020-01-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sale_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
