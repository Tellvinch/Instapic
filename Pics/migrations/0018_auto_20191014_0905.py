# Generated by Django 2.2 on 2019-10-14 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0017_auto_20191014_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='image',
        ),
    ]
