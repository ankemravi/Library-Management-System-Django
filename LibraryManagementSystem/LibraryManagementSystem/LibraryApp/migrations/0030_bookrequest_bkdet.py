# Generated by Django 3.0 on 2023-09-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0029_remove_bookrequest_bkd'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='bkdet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.AddBook'),
        ),
    ]
