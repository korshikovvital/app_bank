# Generated by Django 4.0.1 on 2022-05-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finapp', '0002_product_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photo/%y/%d/%m'),
        ),
    ]
