# Generated by Django 2.2.7 on 2019-12-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0002_running_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='running',
            name='status',
        ),
    ]
