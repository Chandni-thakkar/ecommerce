# Generated by Django 4.1 on 2024-04-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]