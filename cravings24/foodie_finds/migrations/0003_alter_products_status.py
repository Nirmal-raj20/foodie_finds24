# Generated by Django 4.1.7 on 2023-03-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_finds', '0002_remove_products_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-show'),
        ),
    ]