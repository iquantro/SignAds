# Generated by Django 3.0.8 on 2020-07-27 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='description',
            new_name='user_description',
        ),
    ]
