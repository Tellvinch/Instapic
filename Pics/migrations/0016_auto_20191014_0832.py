# Generated by Django 2.2 on 2019-10-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pics', '0015_auto_20191014_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
