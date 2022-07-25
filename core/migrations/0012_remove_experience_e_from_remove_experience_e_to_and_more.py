# Generated by Django 4.0 on 2022-07-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='e_from',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='e_to',
        ),
        migrations.AddField(
            model_name='experience',
            name='e_year',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]