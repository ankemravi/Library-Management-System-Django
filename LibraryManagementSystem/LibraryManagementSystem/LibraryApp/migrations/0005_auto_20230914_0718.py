# Generated by Django 3.0 on 2023-09-14 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0004_addbook_addate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='has_issuebook',
            new_name='has_adregister',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='has_reqbook',
            new_name='has_stregister',
        ),
    ]
