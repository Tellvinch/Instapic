# Generated by Django 2.2 on 2019-10-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0007_auto_20191013_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
