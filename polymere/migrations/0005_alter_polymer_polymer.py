# Generated by Django 4.1 on 2023-10-28 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polymere', '0004_polymer_timestamp_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polymer',
            name='polymer',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
