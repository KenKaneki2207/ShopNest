# Generated by Django 4.2.8 on 2024-01-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNest', '0013_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='solved',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]