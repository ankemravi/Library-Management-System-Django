# Generated by Django 3.0 on 2023-09-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0014_delete_bookrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.PositiveIntegerField(blank=True, max_length=100, null=True)),
                ('bookid', models.PositiveIntegerField(blank=True, max_length=100, null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='IssuedBook',
        ),
    ]
