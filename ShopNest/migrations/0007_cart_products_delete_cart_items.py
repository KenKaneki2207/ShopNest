# Generated by Django 4.2.8 on 2024-01-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNest', '0006_rename_cart_cart_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart_Items',
        ),
    ]
