# Generated by Django 4.2.8 on 2024-01-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNest', '0014_support_solved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='solved',
            field=models.BooleanField(default='False', null=True),
        ),
    ]
