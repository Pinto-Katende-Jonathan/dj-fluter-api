# Generated by Django 4.2 on 2023-04-23 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0004_publication_pub_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='pub_img',
        ),
    ]