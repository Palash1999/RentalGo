# Generated by Django 2.2.1 on 2019-05-22 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20190522_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lname',
            new_name='last_name',
        ),
    ]
