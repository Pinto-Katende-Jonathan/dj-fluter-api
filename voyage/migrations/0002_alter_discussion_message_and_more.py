# Generated by Django 4.2 on 2023-04-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='message',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(max_length=100000),
        ),
    ]
