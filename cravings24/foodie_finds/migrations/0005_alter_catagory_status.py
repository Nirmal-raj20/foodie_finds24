# Generated by Django 4.1.7 on 2023-03-27 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_finds', '0004_alter_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show,1-show'),
        ),
    ]