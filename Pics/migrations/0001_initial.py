# Generated by Django 2.2 on 2019-10-12 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=150)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
            ],
        ),
    ]
