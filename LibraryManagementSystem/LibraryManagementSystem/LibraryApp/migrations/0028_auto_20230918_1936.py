# Generated by Django 3.0 on 2023-09-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0027_auto_20230918_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrequest',
            name='bkd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.AddBook'),
        ),
    ]
