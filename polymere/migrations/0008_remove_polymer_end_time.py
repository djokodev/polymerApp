# Generated by Django 4.1 on 2023-10-29 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polymere', '0007_rename_timestamp_end_polymer_end_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polymer',
            name='end_time',
        ),
    ]
