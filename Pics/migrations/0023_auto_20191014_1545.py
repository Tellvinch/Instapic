# Generated by Django 2.2 on 2019-10-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0022_auto_20191014_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics/'),
        ),
    ]
