# Generated by Django 4.2 on 2023-04-21 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0002_alter_discussion_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='pub_img',
        ),
    ]
