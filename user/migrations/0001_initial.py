# Generated by Django 4.1.8 on 2023-04-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('waranty', models.CharField(max_length=100)),
            ],
        ),
    ]
