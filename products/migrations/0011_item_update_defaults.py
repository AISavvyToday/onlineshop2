# Generated by Django 3.0.3 on 2020-02-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200212_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='update_defaults',
            field=models.BooleanField(default=False),
        ),
    ]