# Generated by Django 2.2 on 2019-10-14 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0018_auto_20191014_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
