# Generated by Django 4.0.4 on 2022-06-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_orders_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=1111111),
        ),
    ]
