# Generated by Django 3.0.8 on 2020-07-28 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200727_1427'),
        ('AdRecords', '0004_text_text_property_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_property_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userProfile'),
        ),
    ]