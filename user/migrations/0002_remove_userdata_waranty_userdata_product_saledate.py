# Generated by Django 4.1.8 on 2023-04-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='waranty',
        ),
        migrations.AddField(
            model_name='userdata',
            name='product_saledate',
            field=models.DateTimeField(null=True),
        ),
    ]
