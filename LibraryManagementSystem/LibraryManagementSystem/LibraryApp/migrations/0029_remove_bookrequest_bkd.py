# Generated by Django 3.0 on 2023-09-18 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0028_auto_20230918_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='bkd',
        ),
    ]
